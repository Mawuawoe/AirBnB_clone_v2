#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"  # set table name
    name = Column(String(128), nullable=False)

    # Establishes a relationship with City objects
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                            cascade="all, delete-orphan",
                            backref="state")
    else:
        @property
        def cities(self):
            """fs getter attribute that returns City instances"""
            import models
            from models.city import City
            values_city = models.storage.all(City).values()
            list_city = []
            for city in values_city:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
