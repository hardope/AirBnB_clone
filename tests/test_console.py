#!/usr/bin/python3
"""Module test_amenity

This Module contains a tests for Amenity Class
"""

import os
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Tests the console app"""
    @classmethod
    def setUpClass(cls) -> None:
        """sets up the test console"""
        cls.cmd = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """removes the file.json temporary file"""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_create_prints_class_name_error(self):
        """tests the create command class name error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create')
            self.assertEqual("** class name missing **\n",
                             output.getvalue())

    def test_create_prints_class_does_not_exist(self):
        """tests the create command class not found error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BModel')
            self.assertEqual("** class doesn't exist **\n",
                             output.getvalue())

    def test_create_creates_an_object(self):
        """tests the create creates an instance"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            id = output.getvalue()
            self.assertNotIn(id, [None, ""])

        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd(f'show BaseModel {id}')
            self.assertIn(id.strip('\n'), output.getvalue())

    def test_show_prints_class_name_error(self):
        """tests the show command class name error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('show')
            self.assertEqual("** class name missing **\n",
                             output.getvalue())

    def test_show_prints_class_does_not_exist(self):
        """tests the show command class not found error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('show BModel')
            self.assertEqual("** class doesn't exist **\n",
                             output.getvalue())

    def test_show_displays_an_object(self):
        """tests the show shows an instance"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            id = output.getvalue().strip('\n')
            self.cmd.onecmd(f'show BaseModel {id}')
            self.assertIn("BaseModel", output.getvalue())

    def test_destroy_prints_class_name_error(self):
        """tests the destroy command class name error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('destroy')
            self.assertEqual("** class name missing **\n",
                             output.getvalue())

    def test_destroy_prints_class_does_not_exist(self):
        """tests the destroy command class not found error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('destroy BModel')
            self.assertEqual("** class doesn't exist **\n",
                             output.getvalue())

    def test_destroy_prints_instance_not_found(self):
        """tests the destroy command prints instance not found error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('destroy BaseModel adfadfadf')
            self.assertIn("** no instance found **", output.getvalue())

    def test_destroy_deletes_an_object(self):
        """tests the destroy deletes a instance"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            id = output.getvalue().strip('\n')
            self.cmd.onecmd(f'destroy BaseModel {id}')
            self.cmd.onecmd(f'show BaseModel {id}')
            self.assertIn("** no instance found **", output.getvalue())

    def test_all_displays_instance_objects(self):
        """tests the all shows instance objects"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            self.cmd.onecmd('create BaseModel')
            self.cmd.onecmd(f'all')
            self.assertIn("BaseModel", output.getvalue())
            self.assertGreaterEqual(output.getvalue().count("BaseModel"), 2)

    def test_all_displays_class_instance_objects(self):
        """tests the all shows instance objects"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            self.cmd.onecmd('create User')
            self.cmd.onecmd(f'all User')
            self.assertIn("User", output.getvalue())
            self.assertNotIn("BaseModel", output.getvalue())

    def test_update_attr_name_missing_error(self):
        """test update command shows attr name missing error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            id = output.getvalue().strip('\n')
            self.cmd.onecmd(f'update BaseModel {id}')
            self.assertIn("** attribute name missing **", output.getvalue())

    def test_update_attr_value_missing_error(self):
        """test update command shows attr val missing error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            id = output.getvalue().strip('\n')
            self.cmd.onecmd(f'update BaseModel {id} fname')
            self.assertIn("** value missing **", output.getvalue())

    def test_update_updates_instance(self):
        """test update command shows attr val missing error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create State')
            id = output.getvalue().strip('\n')
            self.cmd.onecmd(f'update State {id} name example_state')
            self.cmd.onecmd(f'show State {id}')
            self.assertIn('name', output.getvalue())
            self.assertIn('example_state', output.getvalue())

    def test_classname_all_displays_instance_objects(self):
        """tests the all shows instance objects"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            self.cmd.onecmd('create BaseModel')
            self.cmd.onecmd('BaseModel.all()')
            self.assertIn("BaseModel", output.getvalue())
            self.assertGreaterEqual(output.getvalue().count("BaseModel"), 2)

    def test_classname_count_displays_instance_objects(self):
        """tests the all shows instance objects"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create Place')
            self.cmd.onecmd('create Place')
            self.cmd.onecmd('create Place')
            self.cmd.onecmd('create Place')
            self.cmd.onecmd('create Place')
            self.cmd.onecmd('Place.count()')
            self.assertIn('5', output.getvalue())

    def test_classname_show_displays_an_object(self):
        """tests the show shows an instance"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            id = output.getvalue().strip('\n')
            self.cmd.onecmd(f'BaseModel.show("{id}")')
            self.assertIn("BaseModel", output.getvalue())

    def test_classname_destroy_deletes_an_object(self):
        """tests the destroy deletes a instance"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            id = output.getvalue().strip('\n')
            self.cmd.onecmd(f'BaseModel.destroy("{id}")')
            self.cmd.onecmd(f'show BaseModel {id}')
            self.assertIn("** no instance found **", output.getvalue())

    def test_classname_update_updates_instance(self):
        """test update command shows attr val missing error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create Review')
            id = output.getvalue().strip('\n')
            self.cmd.onecmd(f'Review.update("{id}", "rev_k", "rev_v")')
            self.cmd.onecmd(f'show Review {id}')
            self.assertIn('rev_k', output.getvalue())
            self.assertIn('rev_v', output.getvalue())

    def test_classname_update_updates_instance_with_dict(self):
        """test update command shows attr val missing error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create Amenity')
            id = output.getvalue().strip('\n')
            dict_att = "{ 'name' : 'amne', 'rev_k' : 'rev_v' }"
            self.cmd.onecmd(f'Amenity.update("{id}", {dict_att})')
            self.cmd.onecmd(f'show Amenity {id}')
            self.assertIn('name', output.getvalue())
            self.assertIn('amne', output.getvalue())
            self.assertIn('rev_k', output.getvalue())
            self.assertIn('rev_v', output.getvalue())
