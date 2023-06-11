#!/usr/bin/python3
"""This is the Place Module for AirBnB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    metadata = Base.metadata
    place_amenity = Table("place_amenity", metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 nullable=False))


class Place(BaseModel, Base):
    """This is the Class for Place:  A place to stay 
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id', ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review",
                               cascade="all, delete",
                               backref=backref("place", cascade="all, delete"),
                               passive_deletes=True)
        amenities = relationship("Amenity", secondary="place_amenity",
                                 back_populates="place_amenities",
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """Getter attribute in case of file storage
            Return:
                returns list of review instances for file storage
                matching place_id
            """
            from models import storage
            return {k: v for k, v in storage.all().items()
                    if v.place_id == self.id}

        @property
        def amenities(self):
            """
            Getter attribute amenities that returns the list of Amenity
            instances based on the attribute amenity_ids that contains
            all Amenity.id linked to the Place
            """
            from models import storage
            from models.amenity import Amenity

            return [amenity for amenity in storage.all(Amenity).values()
                    if amenity.place_id == self.id]

        @amenities.setter
        def amenities(self, obj):
            """
            Setter attribute amenities that handles append method for adding
            an Amenity.id to the attribute amenity_ids
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
