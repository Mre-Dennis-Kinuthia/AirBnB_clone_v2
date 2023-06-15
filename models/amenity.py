#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class Amenity(BaseModel, Base):
    """
    Amenity Class
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary='place_amenity')
