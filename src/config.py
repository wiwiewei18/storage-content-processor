import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    RABBITMQ_URI = os.getenv("RABBITMQ_URI")
    R2_REGION = os.getenv("R2_REGION")
    R2_ACCOUNT_ID = os.getenv("R2_ACCOUNT_ID")
    R2_ACCESS_KEY = os.getenv("R2_ACCESS_KEY")
    R2_SECRET_KEY = os.getenv("R2_SECRET_KEY")
    R2_BUCKET = os.getenv("R2_BUCKET")

    @property
    def R2_ENDPOINT(self) -> str:
        return f"https://{self.R2_ACCOUNT_ID}.r2.cloudflarestorage.com/{self.R2_BUCKET}"

settings = Settings()