#!/usr/bin/python3
""" This module defines a DB storage
    Class to manage DataBase for AirBnB clone
"""
import datetime
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base


class DBStorage():
    """
    Class manages DataBase Storage of hbnb models in MySQL for AirBnB project
    """
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session and returns all
        objects depending of the class name (argument cls)"""

        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            for clase in classes:
                result = self.__session.query(clase).all()
                dic = {}
                for element in result:
                    key = "{}.{}".format(clase.__name__, element.id)
                    dic[key] = element
            return dic
        else:
            result = self.__session.query(cls).all()
            dic = {}
            for element in result:
                key = "{}.{}".format(cls.__name__, element.id)
                dic[key] = element
            return dic

    def new(self, obj):
        """Add the object to the current database session
        i.e (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session
        i.e (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database(feature of SQLAlchemy)
        create the current database session(self.__session)
        from the engine(self.__engine) by using a sessionmaker"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ to removesSession """
        self.__session.remove()

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
