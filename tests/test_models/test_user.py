#!/usr/bin/python3

from models.user import User
from tests.test_models.test_base_model import test_basemodel
import os


class test_User(test_basemodel):
    """ tests class for user model"""

    def __init__(self, *args, **kwargs):
        """ user test class init"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ tests user first anme attr"""
        new = self.value()
        self.assertEqual(type(new.first_name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_last_name(self):
        """ test user last name attr"""
        new = self.value()
        self.assertEqual(type(new.last_name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_email(self):
        """ test user email attr"""
        new = self.value()
        self.assertEqual(type(new.email), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_password(self):
        """ test user password attr"""
        new = self.value()
        self.assertEqual(type(new.password), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
