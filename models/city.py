#!/usr/bin/python3
"""
City Module for HBNB project
that create the city table
"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, DateTime
from datetime import datetime
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """
        The city class, contains state ID and name
        """
        __tablename__ = 'cities'
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.now)
        updated_at = Column(DateTime, nullable=False, default=datetime.now)
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

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
