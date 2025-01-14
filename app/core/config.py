import os

# Application configurations
class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")
    USERS_FILE: str = "app/database/users.json"
    BILLS_FILE: str = "app/database/bills.json"

settings = Settings()
