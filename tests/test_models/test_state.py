#!/usr/bin/python3
"""Unit test for the state class
Author: Mire
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.my_model = State()
        cls.my_model.name = "Amsterdam"
        cls.my_model.save()

    def test_init(self):
        """Tests for the initialization value of state"""
        self.my_model.name = ""
        self.my_model.save
        model = self.my_model.to_dict()
        self.assertIn('name', model)
        self.assertTrue(self.my_model.id)

    def test_attr(self):
        """Tests that attributes are inserted properly in dict"""

        model = self.my_model.to_dict()
        self.assertEqual(model['name'], self.my_model.name)
        self.assertTrue(self.my_model.id)
        self.assertEqual(model['__class__'], 'State')

    @classmethod
    def tearDownClass(cls):
        del cls.my_model
