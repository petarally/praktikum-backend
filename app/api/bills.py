from fastapi import APIRouter, HTTPException, UploadFile, Form
from pydantic import BaseModel
import json
from core.ocr import extract_text

router = APIRouter()

# Mock bill database (JSON file)
BILL_DB = "app/database/bills.json"

class Bill(BaseModel):
    house: str
    amount: float
    due_date: str
    category: str

@router.post("/")
def add_bill(bill: Bill):
    try:
        with open(BILL_DB, "r+") as f:
            bills = json.load(f)
            bills.append(bill.dict())
            f.seek(0)
            json.dump(bills, f)
        return {"message": "Bill added successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/ocr")
def ocr_bill(file: UploadFile):
    try:
        text = extract_text(file.file)
        return {"message": "OCR processed successfully", "data": text}
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to process OCR")
