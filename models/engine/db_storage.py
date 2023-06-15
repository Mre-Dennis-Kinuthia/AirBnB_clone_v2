#!/usr/bin/python3
"""
This module defines a class to manage database storage for hbnb clone
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
    This class manages storage of hbnb models in a database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the class with the instance attributes
        """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://\
{}:{}@{}/{}'.format(user, passwd, host, db), pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of objects currently in storage
        """
        dict_objs = {}
        if cls is None:
            cls_list = [State, City, User, Place, Review, Amenity]
            for cls in cls_list:
                cls_objs = self.__session.query(cls).all()
                for obj in cls_objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dict_objs[key] = obj
        else:
            cls_objs = self.__session.query(cls).all()

            for obj in cls_objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dict_objs[key] = obj

        return dict_objs

    def new(self, obj):
        """
        Adds a new object to storage dictionary
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Saves objects created to database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object saved in the database
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Loads database from memory
        """
        Base.metadata.create_all(self.__engine)
        sesh_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh_factory)
        self.__session = Session()

    def close(self):
        """
        Closes an open session
        """
        self.__session.close()
