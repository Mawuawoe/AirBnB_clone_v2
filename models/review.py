#!/usr/bin/python3
"""Review module for the HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import os
from datetime import datetime

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class Review(BaseModel, Base):
        """Review classto store review information"""
        __tablename__ = "reviews"
        __table_args__ = {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'latin1'
        }

        # Define columns in the desired order
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.now)
        updated_at = Column(DateTime, nullable=False, default=datetime.now)
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
else:
    class Review(BaseModel):
        """
        if you are to use filestorage
        """
        place_id = ""
        user_id = ""
        text = ""
