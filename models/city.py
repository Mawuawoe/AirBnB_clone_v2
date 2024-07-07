#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    I am creating a table out of this class for mysql
    """
    __tablename__ = 'cities'  # table name
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)

    state = relationship("State", back_populates="cities")
