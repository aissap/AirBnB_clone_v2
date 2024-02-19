#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column,  String
import models
import shlex


class State(BaseModel, Base):
    """State Class"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if models.storage_t == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            cities_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
