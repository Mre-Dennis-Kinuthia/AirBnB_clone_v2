#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from os import getenv
from unittest import skipIf


@skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "Tests for file storage")
class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        new.name = "Wi-Fi"
        self.assertEqual(type(new.name), str)
