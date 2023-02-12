#!/usr/bin/python3
"""This is the file storage class utilizing Json"""

import json
from models.base_model import BaseModel

class FileStorage():
     """This class serializes instances to a JSON file and
     deserializes JSON file to instances
     Attributes:
          __file_path: path to the JSON file
          __objects: objects will be stored
     """
     __file_path = "file.json"
     __objects = {}

     def all(self):
          """returns a dictionary
          Return:
               returns a dictionary of __object
          """
          return self.__objects

     def new(self, obj):
          """sets __object to given obj
          Args:
               obj: given object
          """
          if obj:
               key = "{}.{}".format(type(obj).__name__, obj.id)
               self.__objects[key] = obj

     def save(self):
          """serialize the json obj and save to file
          """
          my_dict = {}
          for key, value in self.__objects.items():
               my_dict[key] = value.to_dict()
          with open(self.__file_path, 'w', encoding="UTF-8") as f:
               json.dump(my_dict, f)

     def reload(self):
          """deserialize the file path to JSON object
          """
          try:
               with open(self.__file_path, 'r', encoding="UTF-8") as f:
                    for key, value in (json.load(f)).items():
                         value = eval(value["__class__"])(**value)
                         self.__objects[key] = value
          except:
               pass