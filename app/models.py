from sqlalchemy import Column, String, Boolean
from app.database import Base

class SwiftCode(Base):
    __tablename__ = "swift_codes"

    swiftCode = Column(String, primary_key=True, index=True)
    address = Column(String)
    bankName = Column(String)
    countryISO2 = Column(String)
    countryName = Column(String)
    isHeadquarter = Column(Boolean)
