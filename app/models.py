from sqlalchemy import Column, Integer, String, Text
from app.database import Base  # We'll define the Base class in database.py

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)