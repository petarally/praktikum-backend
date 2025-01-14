from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json
import bcrypt
import jwt

router = APIRouter()

# Mock user database (JSON file)
USER_DB = "app/database/users.json"
SECRET_KEY = "your_secret_key"

class User(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(user: User):
    try:
        with open(USER_DB, "r+") as f:
            users = json.load(f)
            if user.email in users:
                raise HTTPException(status_code=400, detail="Email already registered.")
            hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
            users[user.email] = hashed_password.decode()
            f.seek(0)
            json.dump(users, f)
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/login")
def login(user: User):
    try:
        with open(USER_DB, "r") as f:
            users = json.load(f)
            if user.email not in users:
                raise HTTPException(status_code=404, detail="User not found.")
            if not bcrypt.checkpw(user.password.encode(), users[user.email].encode()):
                raise HTTPException(status_code=401, detail="Invalid credentials.")
            token = jwt.encode({"email": user.email}, SECRET_KEY, algorithm="HS256")
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
