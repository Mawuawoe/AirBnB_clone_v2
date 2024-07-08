#!/usr/bin/python3
"""
This module defines a class to manage db storage for hbnb clone

"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
from urllib.parse import quote_plus


class DBStorage:
    """
    DBStorage class for interacting with a MySQL database using SQLAlchemy.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the DBStorage instance.
        """
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = quote_plus(os.getenv("HBNB_MYSQL_PWD"))
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        if not all([user, pwd, host, db]):
            raise ValueError("Missing required environment variables for DB connection")

        db_url = f"mysql+mysqldb://{user}:{pwd}@{host}:3306/{db}"
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries the database session for all objects of a specific class or all classes.
        Returns a dictionary of objects keyed by <class name>.<object id>.
        """
        obj_dict = {}
        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)
            if cls and issubclass(cls, Base):
                q_result = self.__session.query(cls).all()
                for obj in q_result:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    obj_dict[key] = obj
        else:
            classes = [State, City]
            for class_type in classes:
                q_result = self.__session.query(class_type).all()
                for obj in q_result:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """
        Adds the object to the current database session (self.__session).

        Args:
            obj: The object to be added to the database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from the current database session if not None.

        Args:
            obj: The object to be deleted from the database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and sets up a new session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
