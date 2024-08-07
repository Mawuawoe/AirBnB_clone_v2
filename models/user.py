#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
import os
from datetime import datetime

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""

        __tablename__ = "users"
        __table_args__ = {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'latin1'
        }

        # Define columns in the desired order
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.now)
        updated_at = Column(DateTime, nullable=False, default=datetime.now)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)

        places = relationship("Place",
                              backref="user",
                              cascade="all, delete-orphan")

        review = relationship("Review",
                              backref="user",
                              cascade="all, delete-orphan")
else:
    class User(BaseModel):
        """
        if usig filestorage
        """
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

        def __init__(self, *args, **kwargs):
            """initializes Amenity"""
            super().__init__(*args, **kwargs)
