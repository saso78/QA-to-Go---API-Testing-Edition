import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')  # Fallback to localhost if missing
    AUTH_TOKEN = os.getenv('AUTH_TOKEN', None)
    TIMEOUT = int(os.getenv('TIMEOUT', 10))  # Optional, fallback to 10 seconds

    @classmethod
    def print_settings(cls):
        print(f"BASE_URL: {cls.BASE_URL}")
        print(f"AUTH_TOKEN: {'Set' if cls.AUTH_TOKEN else 'Not Set'}")
        print(f"TIMEOUT: {cls.TIMEOUT}")
