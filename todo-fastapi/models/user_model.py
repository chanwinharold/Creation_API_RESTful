from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = 'tf_users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String, nullable=True, unique=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))