#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import os
import models


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        __tablename__ = 'amenities'
        """__table_args__ = {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'latin1'
        }"""
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.now)
        updated_at = Column(DateTime, nullable=False, default=datetime.now)
        name = Column(String(128), nullable=False)
else:
    class Amenity(BaseModel):
        name = ""

        def __init__(self, *args, **kwargs):
            """initializes Amenity"""
            super().__init__(*args, **kwargs)
