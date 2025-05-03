
import pandas as pd
from app.schemas import SwiftCodeCreate
from typing import List


def parse_excel(file_path: str) -> List[SwiftCodeCreate]:
    df = pd.read_excel(file_path)

    # Upewniamy się, że kolumny są wielkimi literami
    df["COUNTRY ISO2 CODE"] = df["COUNTRY ISO2 CODE"].str.upper()
    df["COUNTRY NAME"] = df["COUNTRY NAME"].str.upper()

    result = []
    for _, row in df.iterrows():
        is_hq = row["SWIFT CODE"].endswith("XXX")
        item = SwiftCodeCreate(
            address=row["ADDRESS"],
            bankName=row["NAME"],
            countryISO2=row["COUNTRY ISO2 CODE"],
            countryName=row["COUNTRY NAME"],
            isHeadquarter=is_hq,
            swiftCode=row["SWIFT CODE"]
        )
        result.append(item)

    return result
