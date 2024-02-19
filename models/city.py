#!/usr/bin/python3
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    __tablename__ = 'cities'

    places = relationship("Place", backref="city", cascade="all, delete")
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
