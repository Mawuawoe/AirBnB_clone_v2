#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""

        __tablename__ = "users"
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
        email = ""
        _password = ""
        first_name = ""
        last_name = ""
