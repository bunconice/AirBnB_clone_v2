#!/usr/bin/python3

import os
from models.review import Review
from tests.test_models.test_base_model import test_basemodel

class test_review(test_basemodel):
    """ test class review"""

    def __init__(self, *args, **kwargs):
        """ class init review"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """review place_id attr test"""
        new = self.value()
        self.assertEqual(type(new.place_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """review user_id attr test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_text(self):
        """ review text attr test"""
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
