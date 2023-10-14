#!/usr/bin/python3
"""
Unit test for file storage module/class
Author: Mire
"""
import unittest
from models.base_model import BaseModel
from models import storage

class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        my_model_1 = BaseModel()
        my_model_2 = BaseModel()
        my_model_1.save()
        my_model_2.save()
        storage.reload()

    def test_all(self):
        class_name = self.my_model_1.__class__.__name__
        class_name2 = self.my_model_2.__class__.__name__
        self.assertEqual(type(self.my_model_1.all()), f'{class_name}')
        self.assertEqual(type(self.my_model_2.all()), f'{class_name2}')
        
