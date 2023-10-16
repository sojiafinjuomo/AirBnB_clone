#!/usr/bin/python3
"""
child class Review inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    public class attributes are empty string
    """
    place_id = ""
    user_id = ""
    text = ""
