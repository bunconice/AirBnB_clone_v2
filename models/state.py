#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
import models
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



class State(BaseModel, Base):
    """ The state class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """
        method returns the list of City instances with state_id equals
        to the current State.id
        """
        from models import storage
        related_cities = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                related_cities.append(city)
        return related_cities
