import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.environ.get("MONGO_URI")
    MONGO_DBNAME = os.environ.get("MONGO_DBNAME")
    MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")