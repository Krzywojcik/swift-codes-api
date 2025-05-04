
 #Module name:   crud
 #Author:        Krzysztof Wójcik
 #Last modified: 2025-05-03
 #Description:   Database access functions for SWIFT code records.


from sqlalchemy.orm import Session
from app import models, schemas

# Creates a new SWIFT code entry in the database
def create_swift_code(db: Session, code: schemas.SwiftCodeCreate):
    db_code = models.SwiftCode(**code.dict())
    db.add(db_code)
    db.commit()
    db.refresh(db_code)
    return db_code

# Creates a new SWIFT code entry in the database
# If it's a headquarter, also retrieves all its branch codes
# Otherwise, returns only the single matching code
def get_swift_code(db: Session, code: str):
    main = db.query(models.SwiftCode).filter(models.SwiftCode.swiftCode == code).first()
    if main and main.isHeadquarter:
        prefix = main.swiftCode[:8].upper()
        branches = db.query(models.SwiftCode).filter(
            models.SwiftCode.swiftCode != main.swiftCode,
            models.SwiftCode.swiftCode.ilike(f"{prefix}%")
        ).all()
        return main, branches
    return main, []



# Deletes a SWIFT code entry from the database
def delete_swift_code(db: Session, code: str):
    db_code = db.query(models.SwiftCode).filter(models.SwiftCode.swiftCode == code).first()
    if db_code:
        db.delete(db_code)
        db.commit()
    return db_code


# Retrieves all SWIFT codes from the database for a given country code
def get_codes_by_country(db: Session, iso2: str):
    return db.query(models.SwiftCode).filter(models.SwiftCode.countryISO2 == iso2.upper()).all()
