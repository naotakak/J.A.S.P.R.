#J.A.S.P.R.

import sqlite3
from os.path import isfile

path = "data/data.db"

def get_db():
	return sqlite3.connect(path)

def get_cursor(db):
	return db.cursor()

#def insert_into(db, ):
#CREATING THE  TABLE/or connect
if isfile(path):
	pass
else:
	db = sqlite3.connect(path)
	cmd_story = "CREATE TABLE stories(id INT PRIMARY KEY, title TEXT,\
        rest_of_text TEXT, last_text TEXT);"
        cmd_account = "CREATE TABLE account(Username TEXT,Password TEXT,\
        STORIES TEXT, id INT PRIMARY KEY);"

	db.execute(cmd)
	print "makes database here"
#============================================================#
#============================Accounts========================#
#============================================================#
'''
if true, can display the entire story
if false, can only see the latest commit
'''
def can_view(user_id, story_id):
	stories = db.get_list(user_id)
	return story_id in stories 



#Accounts database Functions
def check_account(username):
	command = "SELECT username FROM accounts"
	usernames = c.execute(command)
	for list_username in usernames:
		if list_username == username:
			return False
	return True
	
def create_account(username, password):
	command = "INSERT INTO accounts VALUES (" + username + ", " + password \
        + ", ," + get_ac_id() + " )" 

