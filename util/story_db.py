#J.A.S.P.R.

import sqlite3
from os.path import isfile

path = "../data/stories.db"

def get_db():
	return sqlite3.connect(path)

def get_cursor(db):
	return db.cursor()

#def insert_into(db, ):

if isfile(path):
	pass
else:
	# db = sqlite3.connect(path)
	# cmd = "CREATE TABLE stories(id INT PRIMARY KEY, title TEXT, rest_of_text TEXT, last_text TEXT);"
	# db.execute(cmd)
	print "makes database here"