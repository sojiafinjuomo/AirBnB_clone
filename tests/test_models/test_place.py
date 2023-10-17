#!/usr/bin/python3
"""
Unit test for the Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.my_model = Place()
        cls.my_model.save()

    def test_init(self):
        self.my_model.city_id = ""
        self.my_model.user_id = ""
        self.my_model.name = ""
        self.my_model.description = ""
        self.my_model.number_rooms = 0
        self.my_model.number_bathrooms = 0
        self.my_model.max_guest = 0
        self.my_model.price_by_night = 0
        self.my_model.latitude = 0.0
        self.my_model.longitude = 0.0
        self.my_model.amenity_ids = []

        self.assertEqual(self.my_model.city_id, '')
        self.assertEqual(self.my_model.user_id, '')
        self.assertEqual(self.my_model.name, '')
        self.assertEqual(self.my_model.description, '')
        self.assertEqual(self.my_model.number_rooms, 0)
        self.assertEqual(self.my_model.number_bathrooms, 0)
        self.assertEqual(self.my_model.max_guest, 0)
        self.assertEqual(self.my_model.price_by_night, 0)
        self.assertEqual(self.my_model.latitude, 0.0)
        self.assertEqual(self.my_model.longitude, 0.0)
        self.assertEqual(self.my_model.amenity_ids, [])
        
    def test_attr(self):
        self.my_model.city_id = "dffewfe4fwef"
        self.my_model.user_id = "dffewfe4fwef"
        self.my_model.name = "Mire"
        self.my_model.description = "bugabugabuga"
        self.my_model.number_rooms = 2
        self.my_model.number_bathrooms = 4
        self.my_model.max_guest = 2
        self.my_model.price_by_night = 230
        self.my_model.latitude = 34.7
        self.my_model.longitude = 43.2
        self.my_model.amenity_ids = ['er','rt','dsf']

        self.assertEqual(self.my_model.city_id, 'dffewfe4fwef')
        self.assertEqual(self.my_model.user_id, 'dffewfe4fwef')
        self.assertEqual(self.my_model.name, 'Mire')
        self.assertEqual(self.my_model.description, 'bugabugabuga')
        self.assertEqual(self.my_model.number_rooms, 2)
        self.assertEqual(self.my_model.number_bathrooms, 4)
        self.assertEqual(self.my_model.max_guest, 2)
        self.assertEqual(self.my_model.price_by_night, 230)
        self.assertEqual(self.my_model.latitude, 34.7)
        self.assertEqual(self.my_model.longitude, 43.2)
        self.assertEqual(self.my_model.amenity_ids, ['er','rt','dsf'])

    @classmethod
    def tearDownClass(cls):
        del cls.my_model