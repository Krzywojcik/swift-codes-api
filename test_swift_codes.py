 #Module name:   test_swift_codes
 #Author:        Krzysztof Wójcik
 #Last modified: 2025-05-03
 #Description:   Unit tests for the SWIFT Codes API endpoints using FastAPI's TestClient.

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_code():
    payload = {
        "address": "Test Address",
        "bankName": "Test Bank",
        "countryISO2": "TS",
        "countryName": "TESTLAND",
        "isHeadquarter": True,
        "swiftCode": "TESTBANKXXX"
    }
    response = client.post("/v1/swift-codes", json=payload)
    assert response.status_code == 200
    assert response.json()["swiftCode"] == "TESTBANKXXX"

# Test retrieving the added SWIFT code
def test_get_code():
    response = client.get("/v1/swift-codes/TESTBANKXXX")
    assert response.status_code == 200
    assert response.json()["swiftCode"] == "TESTBANKXXX"
    assert "branches" in response.json()

# Test retrieving SWIFT codes by country
def test_get_by_country():
    response = client.get("/v1/swift-codes/country/TS")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(code["swiftCode"] == "TESTBANKXXX" for code in response.json())

# Test deleting the added SWIFT code
def test_delete_code():
    response = client.delete("/v1/swift-codes/TESTBANKXXX")
    assert response.status_code == 200
    assert response.json()["message"] == "deleted"
