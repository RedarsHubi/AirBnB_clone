"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for BaseModel class."""

    def test_id_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids(self):
        A1 = BaseModel()
        A2 = BaseModel()
        self.assertNotEqual(A1.id, A2.id)

    def test_datetime(self):
        A1 = BaseModel()
        sleep(0.1)
        A2 = BaseModel()
        self.assertNotEqual(A1.created_at, A2.created_at)
