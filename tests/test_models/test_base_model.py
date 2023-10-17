#!/usr/bin/python3
"""
Unit Tests for the Base Model class methods
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Create dummy instances for testing purposes"""
        cls.my_model_1 = BaseModel()
        cls.my_model_2 = BaseModel()

    def test_init(self):
        """Test for proper initialization of attributes"""
        self.assertIsInstance(self.my_model_1.id, str)
        self.assertEqual(type(self.my_model_2.id), str)
        self.assertNotEqual(self.my_model_1.id, self.my_model_2.id)
        self.assertIsInstance(self.my_model_1.updated_at, datetime)
        self.assertIsInstance(self.my_model_1.created_at, datetime)

    def test_str_method(self):
        """Test that the string method __str__ prints the correct result"""

        class_name = self.my_model_1.__class__.__name__
        class_id = self.my_model_1.id
        class_dict = self.my_model_1.__dict__
        str_format = f'[{class_name}] ({class_id}) {class_dict}'
        self.assertEqual(str(self.my_model_1), str(str_format))
        class_name = self.my_model_2.__class__.__name__
        class_id = self.my_model_2.id
        class_dict = self.my_model_2.__dict__
        str_format = f'[{class_name}] ({class_id}) {class_dict}'
        self.assertEqual(str(self.my_model_2), str(str_format))

    def test_save(self):
        """
        Checks that save() method updates the 'updated_at'attribute properly
        """
        old_date_1 = str(self.my_model_1.updated_at)
        old_date_2 = str(self.my_model_2.updated_at)
        self.my_model_1.save()
        self.my_model_2.save()
        new_date_1 = str(self.my_model_1.updated_at)
        new_date_2 = str(self.my_model_2.updated_at)
        self.assertNotEqual(old_date_1, new_date_1)
        self.assertNotEqual(old_date_2, new_date_2)

    def test_to_dict(self):
        """Checks that to_dict() method does all value conversion correctly
        and has the key '__class__' with the classname as value"""
        model_class_1 = self.my_model_1.to_dict()
        model_class_2 = self.my_model_2.to_dict()
        self.assertEqual(type(model_class_1['created_at']), str)
        self.assertEqual(type(model_class_1['updated_at']), str)
        self.assertEqual(type(model_class_2['created_at']), str)
        self.assertEqual(type(model_class_2['updated_at']), str)
        class_name = self.my_model_1.__class__.__name__
        self.assertEqual(model_class_1['__class__'], class_name)
        class_name = self.my_model_2.__class__.__name__
        self.assertEqual(model_class_2['__class__'], class_name)
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        mode_1 = model_class_1['created_at']
        mode_2 = model_class_2['created_at']
        self.assertTrue(datetime.strptime(mode_1, date_format))
        self.assertTrue(datetime.strptime(mode_2, date_format))
        mode_1 = model_class_1['updated_at']
        mode_2 = model_class_2['updated_at']
        self.assertTrue(datetime.strptime(mode_1, date_format))
        self.assertTrue(datetime.strptime(mode_2, date_format))

    @classmethod
    def tearDownClass(cls):
        del cls.my_model_1
        del cls.my_model_2


if __name__ == '__main__':
    unittest.main()
