#!/usr/bin/python3
"""
City Module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class handles all application cities"""
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initialize City"""
        super().__init__(*args, **kwargs)
