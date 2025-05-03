from pydantic import BaseModel

class SwiftCodeBase(BaseModel):
    address: str
    bankName: str
    countryISO2: str
    countryName: str
    isHeadquarter: bool
    swiftCode: str

class SwiftCodeCreate(SwiftCodeBase):
    pass

class SwiftCodeResponse(SwiftCodeBase):
    pass
