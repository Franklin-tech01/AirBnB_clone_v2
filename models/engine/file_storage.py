#!/usr/bin/python3
"""This module defines a class to manage file storage for AirBnB clone"""
#import json


# class FileStorage:
#     """This class manages storage and serializes instances to a
#     JSON file and deserializes JSON file to instances"""
#     __file_path = 'file.json'
#     __objects = {}

#     def all(self, cls=None):
#         """Returns a dictionary of models currently in storage"""
#         if cls is not None:
#             filtered_dict = {}
#             for key, value in self.__objects.items():
#                 if isinstance(value, cls):
#                     filtered_dict[key] = value
#             return filtered_dict
#         return FileStorage.

#     def new(self, obj):
#         """Adds new object to storage dictionary
#         and set __object to given obj"""
#         self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

#     def save(self):
#         """Saves storage dictionary to file"""
#         with open(FileStorage.__file_path, 'w') as f:
#             temp = {}
#             temp.update(FileStorage.__objects)
#             for key, val in temp.items():
#                 temp[key] = val.to_dict()
#             json.dump(temp, f)

#     def reload(self):
#         """Loads storage dictionary from file"""
#         from models.base_model import BaseModel
#         from models.user import User
#         from models.place import Place
#         from models.state import State
#         from models.city import City
#         from models.amenity import Amenity
#         from models.review import Review

#         classes = {
#                     'BaseModel': BaseModel, 'User': User, 'Place': Place,
#                     'State': State, 'City': City, 'Amenity': Amenity,
#                     'Review': Review
#                   }
#         try:
#             temp = {}
#             with open(FileStorage.__file_path, 'r') as f:
#                 temp = json.load(f)
#                 for key, val in temp.items():
#                     self.all()[key] = classes[val['__class__']](**val)
#         except FileNotFoundError:
#             pass

#     def delete(self, obj=None):
#         """Delete obj if it is inside the attribute __objects"""
#         try:
#             key = "{}.{}".format(type(obj).__name__, obj.id)
#             del self.__objects[key]
#             self.save()
#         except FileNotFoundError:
#             pass
#!/usr/bin/python3
""" FileStorage module """

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns the list of objects of one type of class """
        if cls is None:
            return self.__objects
        else:
            objects = {}
            for key, obj in self.__objects.items():
                if type(obj).__name__ == cls.__name__:
                    objects[key] = obj
            return objects
    # def all(self, cls=None):
    #     if cls is None:
    #         return self.__objects
    #     else:
    #         filtered_objects = {}
    #         for obj_id, obj in self.__objects.items():
    #             if type(obj) == cls:
    #                 filtered_objects[obj_id] = obj
    #         return filtered_objects

    def new(self, obj):
        """ Sets in __objects the obj with key """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes obj from __objects if it exists """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    # def delete(self, obj=None):
    #     if obj is not None:
    #         obj_id = obj.__class__.__name__ + "." + obj.id
    #         if obj_id in self.__objects:
    #             del self.__objects[obj_id]


    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes

#!/usr/bin/python3
# """
# Contains the FileStorage class
# """

# import json
# from models.amenity import Amenity
# from models.base_model import BaseModel
# from models.city import City
# from models.place import Place
# from models.review import Review
# from models.state import State
# from models.user import User

# classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
#            "Place": Place, "Review": Review, "State": State, "User": User}


# class FileStorage:
#     """serializes instances to a JSON file & deserializes back to instances"""

#     # string - path to the JSON file
#     __file_path = "file.json"
#     # dictionary - empty but will store all objects by <class name>.id
#     __objects = {}

#     def all(self, cls=None):
#         """returns the dictionary __objects"""
#         if cls is not None:
#             new_dict = {}
#             for key, value in self.__objects.items():
#                 if cls == value.__class__ or cls == value.__class__.__name__:
#                     new_dict[key] = value
#             return new_dict
#         return self.__objects

#     def new(self, obj):
#         """sets in __objects the obj with key <obj class name>.id"""
#         if obj is not None:
#             key = obj.__class__.__name__ + "." + obj.id
#             self.__objects[key] = obj

#     def save(self):
#         """serializes __objects to the JSON file (path: __file_path)"""
#         json_objects = {}
#         for key in self.__objects:
#             json_objects[key] = self.__objects[key].to_dict()
#         with open(self.__file_path, 'w') as f:
#             json.dump(json_objects, f)

#     def reload(self):
#         """deserializes the JSON file to __objects"""
#         try:
#             with open(self.__file_path, 'r') as f:
#                 jo = json.load(f)
#             for key in jo:
#                 self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
#         except:
#             pass

#     def delete(self, obj=None):
#         """delete obj from __objects if it’s inside"""
#         if obj is not None:
#             key = obj.__class__.__name__ + '.' + obj.id
#             if key in self.__objects:
#                 del self.__objects[key]

#     def close(self):
#         """call reload() method for deserializing the JSON file to objects"""
#         self.reload()
