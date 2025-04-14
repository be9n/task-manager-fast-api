from sqlalchemy import Column, Integer, String, Text, Boolean
from app.database import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    is_done = Column(Boolean, default=False)