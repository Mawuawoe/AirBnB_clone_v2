#!/usr/bin/python3
"""
"""
import unittest
import sys
sys.path.append('../../')
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.base_model import BaseModel
from models import storage


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
        self.assertEqual(type(new.name), str)
    
    def test_State_as_subclass(self):
        state = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_State_type(self):
        state = State()
        self.assertEqual(type(state), State)

    def test_add_new_record(self):
        objects = storage.all()
        obt_count_before = len(objects)
        state = State()
        storage.save()
        setattr(state, 'attrname', 'attrvalue')
        storage.save()
        objects = storage.all()
        obt_count_after = len(objects)
        self.assertNotEqual(obt_count_before, obt_count_after)

if __name__ == '__main__':
    unittest.main()
