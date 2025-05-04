
 #Module name:   load_data
 #Author:        Krzysztof Wójcik
 #Last modified: 2025-05-03
 #Description:   Inserts records into the database if they do not exist.


from app.parser import parse_excel
from app.database import SessionLocal, engine
from app.crud import create_swift_code
from app.models import SwiftCode
from app import models


models.Base.metadata.create_all(bind=engine)

file_path = "Interns_2025_SWIFT_CODES.xlsx"

data = parse_excel(file_path)

db = SessionLocal()

# Insert parsed SWIFT codes into the database if they don't already exist
for item in data:
    if not db.query(SwiftCode).filter_by(swiftCode=item.swiftCode).first():
        create_swift_code(db, item)

db.close()
print("Data saved to database.")
