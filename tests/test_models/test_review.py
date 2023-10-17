#!/usr/bin/python3
"""Unit test for the Review class
Author: Mire
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.my_model = Review()
        cls.my_model.save()

    def test_init(self):
        """Tests for the initialization value for review"""
        self.my_model.save
        model = self.my_model.to_dict()
        self.assertIn('place_id', model)
        self.assertIn('user_id', model)
        self.assertIn('text', model)

    def test_attr(self):
        """Tests that attributes are inserted properly in dict"""

        self.my_model.place_id = "sdff34"
        self.my_model.user_id = "ae23dde3"
        self.my_model.text = "i love you"
        model = self.my_model.to_dict()
        self.assertEqual(self.my_model.place_id, 'sdff34')
        self.assertEqual(self.my_model.text, 'i love you')
        self.assertEqual(self.my_model.user_id, 'ae23dde3')
        self.assertTrue(self.my_model.id)
        self.assertEqual(model['__class__'], 'Review')

    @classmethod
    def tearDownClass(cls):
        del cls.my_model
