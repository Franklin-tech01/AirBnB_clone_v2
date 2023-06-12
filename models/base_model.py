# #!/usr/bin/python3
# """This module defines a base class for all models in our hbnb clone"""
# import uuid
# from datetime import datetime
# from sqlalchemy import Column, String, Integer, Table, ForeignKey, DateTime
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


# class BaseModel:
#     """A Base Class for all AirBnB models and defined all common 
#     attributes/methods for other classes"""
#     id = Column(String(60), nullable=False, primary_key=True)
#     created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
#     updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

#     def __init__(self, *args, **kwargs):
#         """Instatntiates a new model class
#         Args:
#             args: it won't be used
#             kwargs: arguments for the constructor of the BaseModel
#         Attributes:
#             id: unique id generated
#             created_at: creation date
#             updated_at: updated date
#         """
#         if not kwargs:
#             from models import storage
#             self.id = str(uuid.uuid4())
#             self.created_at = datetime.now()
#             self.updated_at = datetime.now()
#             # storage.new(self)
#         else:
#             for key, value in kwargs.items():
#                 if key == "created_at" or key == "updated_at":
#                     value = datetime.strptime(kwargs['updated_at'],
#                                               '%Y-%m-%dT%H:%M:%S.%f')
#                 if key != "__class__":
#                     setattr(self, key, value)
#             if "id" not in kwargs:
#                 self.id = str(uuid.uuid4())
#             if "created_at" not in kwargs:
#                 self.created_at = datetime.now()
#             if "updated_at" not in kwargs:
#                 self.updated_at = datetime.now()

#     def __str__(self):
#         """returns a string representation of the instance
#         Return:
#             returns a string of class name, id, and dictionary
#         """
#         cls = (str(type(self)).split('.')[-1]).split('\'')[0]
#         return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

#     def save(self):
#         """Updates the public instance attribute updated_at with 
#         current time when instance is changed"""
#         from models import storage
#         self.updated_at = datetime.now()
#         storage.new(self)
#         storage.save()

#     def to_dict(self):
#         """Convert instance into dict format
#         Return:
#             returns a dictionary of all the key values in __dict__
#         """
#         dictionary = {}
#         dictionary.update(self.__dict__)
#         dictionary.update({'__class__':
#                           (str(type(self)).split('.')[-1]).split('\'')[0]})
#         dictionary['created_at'] = self.created_at.isoformat()
#         dictionary['updated_at'] = self.updated_at.isoformat()
#         if "_sa_instance_state" in dictionary:
#             del dictionary["_sa_instance_state"]
#         return dictionary

#     def delete(self):
#         """deletes current instance from the storage (models.storage) 
#         by calling the method delete()"""
#         import models
#         models.storage.delete(self)

#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)