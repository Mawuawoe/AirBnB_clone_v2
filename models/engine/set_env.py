#!/usr/bin/python3
# import the required dependency
import os


# set env. variable
os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
os.environ['HBNB_MYSQL_PWD'] = 'Driftpiloloo@13'
os.environ['HBNB_MYSQL_HOST'] = 'localhost'
os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'
os.environ['HBNB_TYPE_STORAGE'] = 'db'


# get specific environment variable
user1 = os.environ.get("HBNB_MYSQL_USER")
print(user1)
pwd = os.environ.get('HBNB_MYSQL_PWD')
print(pwd)
host = os.environ.get("HBNB_MYSQL_HOST")
print(host)
db = os.environ.get("HBNB_MYSQL_DB")
print(db)