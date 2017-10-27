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

#============================================================#
#============================Stories=========================#
#============================================================#

def create_story(ID, title, text):
    db = get_db()
    c = get_cursor(db)
    cmd = "INSERT INTO stories VALUES("+ str(ID) + ",'" + title + "','','" + text + "');"
    c.execute(cmd)
    close(db)

def get_ids(): #returns a list of all the id's
	db = get_db()
	c = get_cursor(db)
	ans = c.execute("SELECT id FROM stories;")
	close(db)
	print ans
	return ans

def get_story(ID): #returns full story in text
	db = get_db()
    c = get_cursor(db)
	cmd = "SELECT rest_of_text, last_text FROM stories WHERE id = " + str(ID) +";"
	texts = c.execute(cmd)
	ans = ""
	for text in texts:
		ans+=text
	close(db)
	print ans
	return ans

def get_last(ID):
	db = get_db()
    c = get_cursor(db)
	cmd = "SELECT last_text FROM stories WHERE id = " + str(ID) +";"
	ans = c.execute(cmd)[0]
	close(db)
	print ans
	return ans

def update_story(ID,text):
	db = get_db()
    read = get_cursor(db)
	write = get_cursor(db)
	command = "SELECT rest_of_text FROM stories WHERE id = " + str(ID) +";"
	rest_of_text = read.execute(command)[0]
	command = "SELECT last_text FROM stories WHERE id = " + str(ID) +";"
	last_text = read.execute(command)[0]
    command = "UPDATE stories SET rest_of_text = '" + rest_of_text + last_text + "' WHERE id = " + str(ID) + ";"
    write.execute(cmd)
	command = "UPDATE stories SET last_text = '" + text + "' WHERE id = " + str(ID) + ";"
    write.execute(cmd)
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

