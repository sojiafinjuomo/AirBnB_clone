#!/usr/bin/python3
"""Unit test for the state class
Author: Mire
"""
import unittest
from models.amenity import Amenity


class TestState(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.my_model = Amenity()
        cls.my_model.save()

    def test_init(self):
        """Tests for the initialization value of state"""
        self.my_model.name = ""
        self.my_model.save
        self.assertEqual(self.my_model.name, "")
        model = self.my_model.to_dict()
        self.assertIn('name', model)
        self.assertTrue(self.my_model.id)

    def test_attr(self):
        """Tests that attributes are inserted properly in dict"""

        self.my_model.save()
        model = self.my_model.to_dict()
        self.my_model.name = "Electricity"
        self.assertEqual(self.my_model.name, "Electricity")
        self.my_model.name = "Bore-hole"
        self.assertEqual(self.my_model.name, "Bore-hole")
        self.my_model.name = "Transportation"
        self.assertEqual(self.my_model.name, "Transportation")
        self.my_model.save()
        model = self.my_model.to_dict()
        self.assertEqual(model['name'], "Transportation")
        self.assertTrue(self.my_model.id)
        self.assertEqual(model['__class__'], 'Amenity')

    @classmethod
    def tearDownClass(cls):
        del cls.my_model
