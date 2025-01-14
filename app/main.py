from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import auth, bills

app = FastAPI(
    title="Utility Bill Tracker",
    description="A simple app to track utility bills with OCR support.",
    version="1.0.0",
)

# Allow frontend access
origins = ["http://localhost:3000"]  # Adjust if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(bills.router, prefix="/bills", tags=["Bills"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Utility Bill Tracker API!"}
