from typing import List, Optional
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

class SwiftCodeBranch(BaseModel):
    address: str
    bankName: str
    countryISO2: str
    isHeadquarter: bool
    swiftCode: str

class SwiftCodeWithBranches(SwiftCodeResponse):
    branches: Optional[List[SwiftCodeBranch]] = []
