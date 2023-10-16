#!/usr/bin/python3
"""
User Class (inherits from BaseModel)
Author: Soji & Mire
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user child class inherits from BaseModel
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
