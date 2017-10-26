#J.A.S.P.R.

import sqlite3
from os.path import isfile

path = "data/data.db"

def get_db():
	return sqlite3.connect(path)

def get_cursor(db):
	return db.cursor()

def insert_into(db, ID, title, rest_of_text, last_text):
    cmd = "INSERT INTO stories VALUES("+ str(ID) + ",'" + title + "','" + rest_of_text  + "','" + title + "');"
    print cmd
    print db
    db.execute(cmd)
	
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

