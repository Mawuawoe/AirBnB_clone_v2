#!/usr/bin/python3
from sqlalchemy import create_engine
from urllib.parse import quote_plus

user = 'hbnb_dev'
host = 'localhost'
pwd = quote_plus('Driftpiloloo@13')
db = 'hbnb_dev_db'

db_url = f"mysql+mysqldb://{user}:{pwd}@{host}:3306/{db}"
engine = create_engine(db_url, pool_pre_ping=True)

try:
    connection = engine.connect()
    print("Connection successful")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")
