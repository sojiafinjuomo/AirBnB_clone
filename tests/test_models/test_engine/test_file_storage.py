#!/usr/bin/python3
"""
Unit test for file storage module/class
Author: Mire
"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from pathlib import Path
import json
file_path = './models/engine/storage.json'


class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage Class and methods

	Args:
		unittest (Class): creates unittests
	"""

    @classmethod
    def setUpClass(cls):
        """Sets up testing environment"""
        cls.my_model_1 = BaseModel()
        cls.my_model_2 = BaseModel()
        cls.my_model_1.name = 'mire'
        cls.my_model_2.name = 'ifeanyi'
        cls.my_model_1.city = "Lagos"
        cls.my_model_2.city = "lagos"
        cls.my_model_1.save()
        cls.my_model_2.save()

    def test_all(self):
        """Tests the all method that it returns the correct data
        """
        all_object = storage.all()
        self.assertEqual(type(all_object), dict)
        class_name = f'{self.my_model_1.__class__.__name__}'
        id_num = f'{self.my_model_1.id}'
        key_content = f'{class_name}.{id_num}'
        self.assertEqual(type(all_object[f'{key_content}']), dict)

    def test_new(self):
        """Tests new that it adds new obj to dictionary"""
        new_model = BaseModel()
        new_model.city = "lagos"
        new_model.save()
        model_name = f'{new_model.__class__.__name__}.{new_model.id}'
        self.assertIn(f'{model_name}', storage.all())

    def test_storage_save(self):
        """Tests that the save function in storage store fine"""
        storage.save()
        self.assertTrue(os.path.isfile(file_path))
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.assertEqual(data, storage.all())

    def test_reload(self):
        """Tests the reload function"""
        data = {}
        with open(file_path, 'w') as file:
            json.dump(data, file)
        storage.reload()
        self.assertEqual(storage.all(), {})
        os.remove(file_path)
        self.assertEqual(storage.reload(), None)

    @classmethod
    def tearDownClass(cls):
        """Close testing environment"""
        del cls.my_model_1
        del cls.my_model_2
        Path("./models/engine/storage.json").unlink()
