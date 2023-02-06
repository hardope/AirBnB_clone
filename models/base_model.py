#!/usr/bin/python3
"""This is the base model class for AirBnB project"""
import uuid
from datetime import datetime

import models

class BaseModel:
     """BaseModel Class:
     This class will defines all common attributes/methods
     for other classes
     """
     def __init__(self, *args, **kwargs):
          """Initialize Base class Model with provided information
          Args:
               args: it won't be used
               kwargs: arguments for the constructor of the BaseModel
          Attributes:
               id: unique id generated
               created_at: creation date
               updated_at: updated date
          """
          if kwargs:
               for key, value in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                         value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key != "__class__":
                         setattr(self, key, value)
               if "id" not in kwargs:
                    self.id = str(uuid.uuid4())
               if "created_at" not in kwargs:
                    self.created_at = datetime.now()
               if "updated_at" not in kwargs:
                    self.updated_at = datetime.now()
          else:
               self.id = str(uuid.uuid4())
               self.created_at = self.updated_at = datetime.now()
               models.storage.new(self)

     def __str__(self):
          """String Representation of data in each object
          """
          return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
          
     def save(self):
          """updates the public instance attribute updated_at to current time
          """
          self.updated_at = datetime.now()
          models.storage.save()

     def to_dict(self):
          """creates dictionary of the class  and returns
          a dictionary of all the key values in __dict__
          """
          my_dict = dict(self.__dict__)
          my_dict["__class__"] = str(type(self).__name__)
          my_dict["created_at"] = self.created_at.isoformat()
          my_dict["updated_at"] = self.updated_at.isoformat()
          if '_sa_instance_state' in my_dict.keys():
               del my_dict['_sa_instance_state']
          return my_dict