from sqlalchemy.orm import Session
from app import models, schemas

def create_swift_code(db: Session, code: schemas.SwiftCodeCreate):
    db_code = models.SwiftCode(**code.dict())
    db.add(db_code)
    db.commit()
    db.refresh(db_code)
    return db_code

def get_swift_code(db: Session, code: str):
    return db.query(models.SwiftCode).filter(models.SwiftCode.swiftCode == code).first()

def delete_swift_code(db: Session, code: str):
    db_code = db.query(models.SwiftCode).filter(models.SwiftCode.swiftCode == code).first()
    if db_code:
        db.delete(db_code)
        db.commit()
    return db_code

def get_codes_by_country(db: Session, iso2: str):
    return db.query(models.SwiftCode).filter(models.SwiftCode.countryISO2 == iso2.upper()).all()
