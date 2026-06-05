from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import dotenv, os

dotenv.load_dotenv(dotenv_path='.env')
engine = create_engine(os.getenv('DATABASE_URL') or "")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


import psycopg
from psycopg.rows import dict_row
import dotenv
import os


dotenv.load_dotenv(dotenv_path=".env")

DB_URI=os.getenv('DATABASE_URL')
DB_URL=(f"dbname={os.getenv('DATABASE_NAME')} "
        f"user={os.getenv('DATABASE_USER')} "
        f"host={os.getenv('DATABASE_HOST')} "
        f"port={os.getenv('DATABASE_PORT')} "
        f"password={os.getenv('DATABASE_PASSWORD')}")

class DBConnect:
    def __init__(self):
        self.conn_ = None
        self.curs_ = None

    def open(self):
        self.conn_ = psycopg.connect(DB_URI or DB_URL, row_factory=dict_row)
        self.curs_ = self.conn_.cursor()

    def close(self):
        self.conn_.close()

    def connect(self):
        try:
            self.open()
            self.curs_.execute("""SELECT 1""")
            print("\n\t✅ Connexion à la base de donnée réussie.\n")

        except Exception as error:
            print("\n\t❌ Échec de connexion à la base de données\n")
            raise Exception(error)

db = DBConnect()
db.connect()