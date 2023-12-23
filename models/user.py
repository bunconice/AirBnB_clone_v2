#!/usr/bin/python3
"""Module defines a class User"""

from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='user')

    reviews = relationship('Review', cascade='all, delete, delete-orphan',
                           backref='user')
