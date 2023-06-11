#!/usr/bin/python3
"""This is the  City Module for AirBnB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel, Base):
    """The city class, contains state ID and name
    Attributes:
        state_id: The state id
        name: input name
    """
     __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
                      ForeignKey("states.id", ondelete="CASCADE"),
                      nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete-orphan",
                          passive_deletes=True)
