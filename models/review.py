#!/usr/bin/python3
"""This is the Review module for the AirBnB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review Class to store review information
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    text = Column(String(1024),
                  nullable=False)
    place_id = Column(String(60),
                      ForeignKey("places.id", ondelete="CASCADE"),
                      nullable=False)
    user_id = Column(String(60),
                     ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
