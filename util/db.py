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
        db = sqlite3.connect("data.db")
        c = db.cursor()
	stories = get_list_ac(user_id,c)
	return story_id in stories


def get_list_ac(user_id, c):
        data = c.execute("SELECT stories FROM accounts WHERE id = ?", user_id)
        list = []
        list = data[0].spilt(',')
        list = map(int, list)
        

def check_account(username):
        db = sqlite3.connect("data.db")
        c = db.cursor()
	command = "SELECT username FROM accounts"
	usernames = c.execute(command)
	for list_username in usernames:
		if list_username == username:
			return False
	return True
	
def create_account(username, password):
        db = get_db()
        c = get_cursor(db)
	command = "INSERT INTO accounts VALUES (" + username + ", " + password \
        + ",," + new_ac_id(c) + " )"
        close(db)

def new_ac_id(c):
        db = get_db()
        c = get_cursor(db)
        if
        command = "SELECT COUNT(*) FROM accounts"
        new_id = c.execute(command) 
        return new_id
        
        

