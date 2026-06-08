from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import dotenv, os

dotenv.load_dotenv(dotenv_path='.env')
url_db = os.getenv('DATABASE_URL') or ""
engine = create_engine(url_db)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db_ = SessionLocal()
    try:
        yield db_
    finally:
        db_.close()