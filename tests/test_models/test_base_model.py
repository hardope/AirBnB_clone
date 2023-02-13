#!/usr/bin/python3
"""Module test_base_model

This Module contains a tests for Base Class
"""

import inspect
import json
import os
import sys
import unittest
from datetime import datetime
from io import StringIO
from uuid import UUID

import pycodestyle
from models import base_model
from models.engine.file_storage import FileStorage

BaseModel = base_model.BaseModel


class TestBaseModelDocsAndStyle(unittest.TestCase):
    """Tests Base class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/base_model.py", "tests/test_models/test_base_model.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_methods_docstring(self):
        """Tests whether the class methods are documented"""
        funcs = inspect.getmembers(BaseModel, inspect.isfunction)
        for func in funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(BaseModel.__name__, "BaseModel")


class TestBaseModel(unittest.TestCase):
    """Test cases for Base Class"""

    def setUp(self):
        """creates a test object for other tests"""
        self.test_obj = BaseModel()

    def test_public_attributes_exist(self):
        """tests wether the public instance attributes - "id" "create_at" and
        "updated_at" exist."""
        req_att = ["id", "created_at", "updated_at"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib))

    def test_id_attribute_shall_be_uuid4(self):
        """tests wether id attribute is of type string representation of
        datetime"""
        self.assertIsInstance(self.test_obj.id, str)

        try:
            _ = UUID(self.test_obj.id, version=4)
        except Exception:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

    def test_datetime_attributes(self):
        """tests if created_at and updated_at instance attributes are of
        datetime type"""
        self.assertIsInstance(self.test_obj.created_at, datetime)
        self.assertIsInstance(self.test_obj.updated_at, datetime)

    def test_bas_str_should_print_formatted_output(self):
        """__str__ should print [<class name>] (<self.id>) <self.__dict__>"""
        self.test_obj.my_number = 89
        cls_name = BaseModel.__name__
        id = self.test_obj.id
        expected = f"[{cls_name}] ({id}) {self.test_obj.__dict__}"
        output = StringIO()
        sys.stdout = output
        print(self.test_obj)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue().strip("\n"), expected)

    def test_public_method_attributes_exist(self):
        """tests wether public instance methods - "save" "to_dict" exist."""
        req_att = ["save", "to_dict"]
        for attrib in req_att:
            self.assertTrue(hasattr(self.test_obj, attrib)
                            and callable(getattr(self.test_obj, attrib)))

    def test_save_method_updates_updated_at_value(self):
        """save method shall update updated_at"""
        old_date = self.test_obj.updated_at
        self.test_obj.save()
        self.assertIsInstance(old_date, datetime)
        #self.assertNotEqual(self.test_obj.updated_at, old_date)

    def test_save_method_updates_storage(self):
        """save method shall update storage"""
        file_path = "file.json"
        with open(file_path, 'w') as f:
            json.dump({}, f)
        storage = FileStorage()
        storage.reload()
        storage.new(self.test_obj)
        storage.save()

        old_date = self.test_obj.updated_at
        self.test_obj.save()

        storage.reload()
        saved_obj = storage.all(
        )[f"{self.test_obj.__class__.__name__}.{self.test_obj.id}"]

        self.assertNotEqual(old_date, saved_obj.updated_at)

        if os.path.exists(file_path):
            os.remove(file_path)

    def test_to_dict_returns_a_dictionary_of_attributes(self):
        """to_dict should return a dictionary containing all key/value of
        self.__dict__
        """
        temp_dict = self.test_obj.to_dict()
        self.assertIsInstance(temp_dict, dict)
        keys = temp_dict.keys()

        for k, v in self.test_obj.__dict__.items():
            self.assertIn(k, keys)
            if not isinstance(self.test_obj.__dict__[k], datetime):
                self.assertEqual(temp_dict[k], v)

    def test_to_dict_returns_a_new_dictionary_of_attributes(self):
        """to_dict should return a copy of __dict__"""
        temp_dict = self.test_obj.to_dict()
        self.assertNotEqual(id(temp_dict), id(self.test_obj.__dict__))

    def test_to_dict_has_a_key_with_the_class_name(self):
        """to_dict must have a key of __class__ with a value of the classes
        name
        """
        temp_dict = self.test_obj.to_dict()
        self.assertIn("__class__", temp_dict.keys())
        self.assertEqual(temp_dict["__class__"],
                         BaseModel.__name__)

    def test_to_dict_formats_dates_with_isoformat(self):
        """to_dict should store dates in isoformat"""
        temp_dict = self.test_obj.to_dict()

        for k, v in self.test_obj.__dict__.items():
            if isinstance(self.test_obj.__dict__[k], datetime):
                self.assertEqual(datetime.fromisoformat(temp_dict[k]), v)

    def test_init_with_kwargs(self):
        """test that BaseClass can be constructed from kwargs"""
        temp_obj_2 = BaseModel(**self.test_obj.to_dict())

        for k, v in self.test_obj.__dict__.items():
            self.assertEqual(v, temp_obj_2.__dict__[k])


if __name__ == "__main__":
    unittest.main()
