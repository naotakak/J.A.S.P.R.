#J.A.S.P.R.

import sqlite3
from os.path import isfile

path = "data/data.db"

def get_db():
	return sqlite3.connect(path)

def get_cursor(db):
	return db.cursor()

def close(db):
    db.commit()
    db.close()

def insert_into_s(ID, title, rest_of_text, last_text):
    db = get_db()
    c = get_cursor(db)
    cmd = "INSERT INTO stories VALUES("+ str(ID) + ",'" + title + "','" + rest_of_text  + "','" + last_text + "');"
    print cmd
    print c
    c.execute(cmd)
    close(db)
	
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

