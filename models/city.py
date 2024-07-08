#!/usr/bin/python3
"""
City Module for HBNB project
that create the city table
"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """
        The city class, contains state ID and name
        """
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)

        places = relationship("Place",
                            backref="cities",
                            cascade="all, delete-orphan")
else:
    class City(BaseModel):
        """
        if usig file storge
        """
        name = ""
        state_id = ""

        def __init__(self, *args, **kwargs):
            """initializes Amenity"""
            super().__init__(*args, **kwargs)
