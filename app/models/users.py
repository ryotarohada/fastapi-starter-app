from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    name = Column(String(20), nullable=False, default="default_name")
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
