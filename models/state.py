#!/usr/bin/python3
"""
State Module for HBNB project
craete and populate the state table
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """
        State class, that create the state table
        column name and id
        """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)

        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            cities = relationship("City",
                              cascade="all, delete-orphan",
                              backref="state")
else:
    class State(BaseModel):
        name = ""

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
