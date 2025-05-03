from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/v1/swift-codes/{swift_code}", response_model=schemas.SwiftCodeWithBranches)
def get_code(swift_code: str, db: Session = Depends(get_db)):
    main, branches = crud.get_swift_code(db, swift_code)
    if not main:
        raise HTTPException(status_code=404, detail="Not found")

    response = schemas.SwiftCodeWithBranches(**main.__dict__)
    response.branches = [schemas.SwiftCodeBranch(**b.__dict__) for b in branches]
    return response

@app.get("/v1/swift-codes/country/{country_code}", response_model=List[schemas.SwiftCodeResponse])
def get_by_country(country_code: str, db: Session = Depends(get_db)):
    return crud.get_codes_by_country(db, country_code)

@app.post("/v1/swift-codes", response_model=schemas.SwiftCodeResponse)
def add_code(code: schemas.SwiftCodeCreate, db: Session = Depends(get_db)):
    return crud.create_swift_code(db, code)

@app.delete("/v1/swift-codes/{swift_code}")
def delete_code(swift_code: str, db: Session = Depends(get_db)):
    deleted = crud.delete_swift_code(db, swift_code)
    if not deleted:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "deleted"}
