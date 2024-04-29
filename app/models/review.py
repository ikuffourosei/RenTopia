#!/usr/bin/python3
"""
Module for the Review section
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import Base


class Review(Base):
    """
    This is the table for the review section
    """

    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    apartment_id = Column(Integer, ForeignKey('apartments.id'))
    rating = Column(Integer)
    comment = Column(String(256))


    user = relationship("User", back_populates="reviews")
    apartment = relationship("Apartment", back_populates="reviews")