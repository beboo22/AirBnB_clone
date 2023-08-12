#!/usr/bin/python3
"""Unit tests for the amenity module.
"""
import os
import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage.FileStorage_objects = {}
        if os.path.exists(FileStorage.FileStorage_file_path):
            os.remove(FileStorage.FileStorage_file_path)

    def test_params(self):
        """Test method for class attributes"""

        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        a3 = Amenity("hello", "wait", "in")

        k = f"{type(a1).name}.{a1.id}"
        self.assertIsInstance(a1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(a3.name, "")

    def test_init(self):
        """Test method for public instances"""
        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        self.assertIsInstance(a1.id, str)
        self.assertIsInstance(a1.created_at, datetime)
        self.assertIsInstance(a1.updated_at, datetime)
        self.assertEqual(a1.updated_at, a2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        a1 = Amenity()
        string = f"[{type(a1).name}] ({a1.id}) {a1.dict}"
        self.assertEqual(a1.str(), string)

    def test_save(self):
        """Test method for save"""
        a1 = Amenity()
        old_update = a1.updated_at
        a1.save()
        self.assertNotEqual(a1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        a_dict = a2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['class'], type(a2).name)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(a1, a2)


if name == "main":
    unittest.main()
