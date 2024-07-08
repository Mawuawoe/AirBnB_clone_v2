import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
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

        db_url = f"mysql+mysqldb://{user}:{pwd}@{host}:3306/{db}"
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        
        """
        """obj_list = []
        obj_dict = {}
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if isinstance(cls, Base):
                obj_list = self.__session.query(cls).all()
            else:
                for subclass in Base.__subclasses__():
                    obj_list.extend(self.__session.query(subclass).all())
  
            for obj in obj_list:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict"""


        obj_dict = {}
        if cls is None:
            classes = [State, City]
            for class_type in classes:
                q_result = self.__session.query(class_type).all()
                for obj in q_result:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    obj_dict[key] = obj
        else:
            q_result = self.__session.query(cls).all()
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
        # if not self.__session:
        #    self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and sets up a new session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
