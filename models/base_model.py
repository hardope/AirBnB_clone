#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
from datetime import datetime

class BaseModel:
     """This class will defines all common attributes/methods
     for other classes
     """
     def __init__(self):
          """Initialize Base class Model
          """
          self.id = str(uuid.uuid4())
          self.created_at = self.updated_at = datetime.now()

     def __str__(self):
          """String Representation of data in each object
          """
          return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
          
     def save(self):
          """updates the public instance attribute updated_at to current time
          """
          self.updated_at = datetime.now()

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