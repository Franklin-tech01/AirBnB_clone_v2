#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """This is the State Class
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all,delete,delete-orphan",
        backref=backref("state", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter attribute in case of file storage-
            returns list of city instances"""
            from models import storage
            from models.city import City
            list_city = []
            for city in storage.all(City):
                if self.id is city.state_id:
                    list_city.append(city)
            return list_city
