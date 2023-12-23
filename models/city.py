#!/usr/bin/python3
""" The city Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


from models.place import Place


class City(BaseModel, Base):
    """ city class, and it contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='cities')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
