#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from os import getenv
from unittest import skipIf


@skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "Tests for file storage")
class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        new.name = "California"
        self.assertEqual(type(new.name), str)
