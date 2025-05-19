from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_SCHEMA = os.getenv("DB_SCHEMA")

connection_string = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_SCHEMA}'

engine = create_engine(connection_string)