#!/usr/bin/python3
"""
User Module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User class handles all application users"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    reviews = relationship("Review", cascade="all, delete",
                           backref="user", passive_deletes=True)

    def __init__(self, *args, **kwargs):
        """initialize User"""
        super().__init__(*args, **kwargs)
