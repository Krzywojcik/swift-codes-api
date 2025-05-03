from app.parser import parse_excel
from app.database import SessionLocal
from app.crud import create_swift_code
from app.models import SwiftCode

file_path = "Interns_2025_SWIFT_CODES.xlsx"
data = parse_excel(file_path)

db = SessionLocal()

for item in data:
    if not db.query(SwiftCode).filter_by(swiftCode=item.swiftCode).first():
        create_swift_code(db, item)

db.close()
print("✅ Dane zostały zapisane do bazy danych.")
