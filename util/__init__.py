import sqlite3
from os.path import isfile
path = "data/data.db"
def creato():
	if isfile(path):
		print "already a database"
	else:
		db = sqlite3.connect(path)
		cmd_story = "CREATE TABLE stories(id INT PRIMARY KEY, title TEXT,\
		rest_of_text TEXT, last_text TEXT);"
		cmd_account = "CREATE TABLE accounts(Username TEXT,Password TEXT,\
		STORIES TEXT, id INT PRIMARY KEY);"

		db.execute(cmd_story)
		db.execute(cmd_account)
		print "makes database here"


creato()
