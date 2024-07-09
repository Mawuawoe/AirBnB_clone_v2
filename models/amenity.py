#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
import os
import models


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
else:
    class Amenity(BaseModel):
        name = ""

        def __init__(self, *args, **kwargs):
            """initializes Amenity"""
            super().__init__(*args, **kwargs)
