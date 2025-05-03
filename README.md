# **SWIFT Codes API**
***Remitly Interns Project***
## Project Description

REST API for parsing, storing, and accessing SWIFT bank codes from an Excel file.

## Tech stack
- Python 3.9
- FastAPI
- SQLite (via SQLAlchemy)
- Pandas + Openpyxl

## ️ How to run

1. Install dependencies:
pip install -r requirements.txt

2. Import Excel data

To load SWIFT codes from the Excel file:

```
python load_data.py
```

Make sure the file "Interns_2025_SWIFT_CODES.xlsx" is in the root folder of the project.

3. Start the server:
python -m uvicorn app.main:app --reload --port 8080

4. Open docs:
```
http://localhost:8080/docs
```
# Endpoints

## **POST /v1/swift-codes**


 Add a new SWIFT code

## **GET /v1/swift-codes/{swift_code}**


 Get details of a specific SWIFT code

## **GET /v1/swift-codes/country/{countryISO2}**


 Get all SWIFT codes for a specific country

## **DELETE /v1/swift-codes/{swift_code}**


 Delete a SWIFT code

