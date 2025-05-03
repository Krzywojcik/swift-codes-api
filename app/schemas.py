from typing import Optional, List
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

class SwiftCodeBranch(BaseModel):
    address: str
    bankName: str
    countryISO2: str
    isHeadquarter: bool
    swiftCode: str

class SwiftCodeResponse(SwiftCodeBase):
    pass

class SwiftCodeWithBranches(SwiftCodeResponse):
    branches: Optional[List[SwiftCodeBranch]] = []
