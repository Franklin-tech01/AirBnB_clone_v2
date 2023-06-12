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
                if isinstance(obj, cls):
                    objects[key] = obj
            return objects

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

    def close(self):
        """ Deserializes the JSON file to objects """
        self.reload()

    def classes(self):
        """ Returns a dictionary of valid classes and their references """
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        return classes

    def attributes(self):
        """ Returns the valid attributes and their types for each class """
        attributes = {
            'BaseModel': {
                'id': str,
                'created_at': datetime.datetime,
                'updated_at': datetime.datetime
            },
            'User': {
                'email': str,
                'password': str,
                'first_name': str,
                'last_name': str
            },
            'State': {
                'name': str
            },
            'City': {
                'state_id': str,
                'name': str
            },
            'Amenity': {
                'name': str
            },
            'Place': {
                'city_id': str,
                'user_id': str,
                'name': str,
                'description': str,
                'number_rooms': int,
                'number_bathrooms': int,
                'max_guest': int,
                'price_by_night': int,
                'latitude': float,
                'longitude': float,
                'amenity_ids': list
            },
            'Review': {
                'place_id': str,
                'user_id': str,
                'text': str
            }
        }