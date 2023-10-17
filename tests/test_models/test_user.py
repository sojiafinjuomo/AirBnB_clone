#!/usr/bin/python3
"""
Unit Tests for the Base Model class methods
"""
import unittest
from models.user import User
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Create dummy instances for testing purposes"""
        cls.my_model_1 = User()

    def test_init(self):
        """Test for proper initialization of attributes"""
        self.assertIn('first_name', self.my_model_1.to_dict())
        self.assertIn('last_name', self.my_model_1.to_dict())
        self.assertIn('password', self.my_model_1.to_dict())
        self.assertIn('email', self.my_model_1.to_dict())
        self.assertTrue(self.my_model_1.updated_at)
        self.assertTrue(self.my_model_1.created_at)

    def test_attr(self):
        """Test that the attributes are all present and update accordingly"""

        self.my_model_1.first_name = "Mirey"
        self.my_model_1.last_name = "Amah"
        self.my_model_1.email = "amahe8664@gmail.com"
        self.my_model_1.password = "erfsfsvsddgdgddgerr"
        
        self.assertEqual(self.my_model_1.first_name, "Mirey")
        self.assertEqual(self.my_model_1.last_name, "Amah")
        self.assertEqual(self.my_model_1.email, "amahe8664@gmail.com")
        self.assertEqual(self.my_model_1.password, "erfsfsvsddgdgddgerr")

    def test_to_dict(self):
        """Checks that to_dict() method does all value conversion correctly
        and has the key '__class__' with the classname as value"""
        model_class = self.my_model_1.to_dict()
        self.assertEqual(model_class['__class__'], 'User')
        self.assertEqual(model_class['first_name'], "Mirey")
        self.assertEqual(model_class['last_name'], "Amah")
        self.assertEqual(model_class['email'], "amahe8664@gmail.com")
        self.assertEqual(model_class['password'], "erfsfsvsddgdgddgerr")

    @classmethod
    def tearDownClass(cls):
        del cls.my_model_1


if __name__ == '__main__':
    unittest.main()
