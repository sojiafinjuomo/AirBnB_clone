#!/usr/bin/python3
"""Unit test for the state class
Author: Mire
"""
import unittest
from models.state import State
from models.city import City

class TestCity(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.my_state = State()
        cls.my_state.name = "Amsterdam"
        cls.my_state.save()
        cls.my_city = City()
        cls.my_city.name = "Oud-Zuid"
        cls.my_city.state_id = cls.my_state.id
        cls.my_city.save()

    def test_init(self):
        """Tests for the initialization value of state"""
        self.my_city.name = ""
        self.my_city.state_id = ""
        self.my_city.save
        model = self.my_city.to_dict()
        self.assertEqual(self.my_city.name, "")
        self.assertEqual(self.my_city.state_id, "")
        self.assertIn('name', model)
        self.assertIn('state_id', model)
        self.assertTrue(self.my_city.id)

    def test_attr(self):
        """Tests that attributes are inserted properly in dict"""
        self.my_city.name = "Oud-Zuid"
        self.my_city.state_id = self.my_state.id
        model = self.my_city.to_dict()
        self.assertEqual(model['name'], self.my_city.name)
        self.assertEqual(self.my_city.state_id, self.my_state.id)
        self.assertEqual(self.my_city.name, "Oud-Zuid")
        self.assertEqual(model['__class__'], 'City')

    @classmethod
    def tearDownClass(cls):
        del cls.my_city
        del cls.my_state
