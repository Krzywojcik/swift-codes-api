 #Module name:   test_integration
 #Author:        Krzysztof Wójcik
 #Last modified: 2025-05-03
 #Description:   Contains integration tests using an in-memory SQLite database
 #               to simulate the full application flow for the SWIFT Codes API.

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)

# Full end-to-end test for the entire SWIFT code flow
def test_full_flow(client):
    payload = {
        "address": "HQ Address",
        "bankName": "HQ Bank",
        "countryISO2": "HQ",
        "countryName": "HEADQUARTERLAND",
        "isHeadquarter": True,
        "swiftCode": "HQBANKXXX"
    }

    # Create a new SWIFT code
    response = client.post("/v1/swift-codes", json=payload)
    assert response.status_code == 200

    # Retrieve the created SWIFT code
    response = client.get("/v1/swift-codes/HQBANKXXX")
    assert response.status_code == 200
    assert response.json()["swiftCode"] == "HQBANKXXX"
    assert response.json()["branches"] == []

    # Fetch codes for the country
    response = client.get("/v1/swift-codes/country/HQ")
    assert response.status_code == 200
    assert any(code["swiftCode"] == "HQBANKXXX" for code in response.json())

    # Delete the SWIFT code
    response = client.delete("/v1/swift-codes/HQBANKXXX")
    assert response.status_code == 200
    assert response.json()["message"] == "deleted"
