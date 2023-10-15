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
    @classmethod
    def setUpClass(cls):
        cls.my_model_1 = BaseModel()
        cls.my_model_2 = BaseModel()
        cls.my_model_1.name = 'mire'
        cls.my_model_2.name = 'ifeanyi'
        cls.my_model_1.city = "Lagos"
        cls.my_model_2.city = "lagos"
        cls.my_model_1.save()
        cls.my_model_2.save()
        storage.reload()

    def test_all(self):
        all_object = storage.all()
        self.assertEqual(type(all_object), dict)
        class_name = f'{self.my_model_1.__class__.__name__}
        id_num = {self.my_model_1.id}'
        key_content = f'{class_name}.{id_num}'
        self.assertEqual(type(all_object[f'{key_content}']), dict)

    def test_new(self):
        new_model = BaseModel()
        new_model.city = "lagos"
        new_model.save()
        model_name = f'{new_model.__class__.__name__}.{new_model.id}'
        self.assertIn(f'{model_name}', storage.all())

    def test_storage_save(self):
        storage.save()
        self.assertTrue(os.path.isfile(file_path))
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.assertEqual(data, storage.all())

    def test_reload(self):
        data = {}
        with open(file_path, 'w') as file:
            json.dump(data, file)
        storage.reload()
        self.assertEqual(storage.all(), {})
        os.remove(file_path)
        self.assertEqual(storage.reload(), None)

    @classmethod
    def tearDownClass(cls):
        del cls.my_model_1
        del cls.my_model_2
        Path("./models/engine/storage.json").unlink()
