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

def create_story(ID, title, rest_text, last_text):
	db = get_db()
	c = get_cursor(db)
	cmd = "INSERT INTO stories VALUES("+ str(ID) + ",'" + title + "','" + rest_text + "','" + last_text + "');"
	print cmd
	c.execute(cmd)
	close(db)

def get_ids(): #returns a list of all the id's
	db = get_db()
	c = get_cursor(db)
	ans = c.execute("SELECT id FROM stories;").fetchall()
	close(db)
	print ans
	return ans

def get_story(ID): #returns full story in text
	db = get_db()
	c = get_cursor(db)
	cmd = "SELECT title, rest_of_text, last_text FROM stories WHERE id = " + str(ID) +";"
	text = c.execute(cmd).fetchone()
	ans = [text[0], text[1], text[2]]
	print ans
	return ans

def get_last(ID):
	db = get_db()
	c = get_cursor(db)
	cmd = "SELECT last_text FROM stories WHERE id = " + str(ID) +";"
	result = c.execute(cmd).fetchone()
	ans = result[0]
	close(db)
	print ans
	return ans

def update_story(ID,text):
	db = get_db()
	read = get_cursor(db)
	write = get_cursor(db)
	command = "SELECT rest_of_text FROM stories WHERE id = " + str(ID) +";"
	rest_of_text = read.execute(command).fetchone()[0]
	command = "SELECT last_text FROM stories WHERE id = " + str(ID) +";"
	last_text = read.execute(command).fetchone()[0]
	cmd = "UPDATE stories SET rest_of_text = '" + rest_of_text + " " +  last_text + "' WHERE id = " + str(ID) + ";"
	write.execute(cmd)
	cmd = "UPDATE stories SET last_text = '" + text + "' WHERE id = " + str(ID) + ";"
	write.execute(cmd)
	close(db)

def print_stories():
	db = get_db()
	c = get_cursor(db)
	command = "SELECT * FROM stories"
	result = c.execute(command)
	for story in result:
		print story

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

'''
grabs the list of stories from an userid
'''
def get_list_ac(user_id, c):
	data = c.execute("SELECT stories FROM accounts WHERE id = ?", user_id)
	list = []
	list = data[0].spilt(',')
	list = map(int, list)

'''
sees if a username is in the database
'''
def check_account_exist(username):
	db = get_db()
	c = get_cursor(db)
	command = "SELECT username FROM accounts WHERE username = \"" + username + "\""
	usernames = c.execute(command)
	for list_username in usernames:
		return list_username != None
	return False
'''
update the table with a new account
'''
def create_account(username, password):
	db = get_db()
	c = get_cursor(db)
	command = "INSERT INTO accounts VALUES (\"" + username + "\", \"" + password + "\"," + "\"\"" + ", " + str(new_ac_id()) + " )"
	print command
	c.execute(command)
	close(db)
'''
gets new id using num # rows
'''
def new_ac_id():
	db = get_db()
	c = get_cursor(db)
	command = "SELECT COUNT(*) FROM accounts"
	result = c.execute(command).fetchone()
	count = result[0]
	#print count
	return count
'''
authenticates username and password
'''
def check_account(username, password):
	db = get_db()
	c = get_cursor(db)
	if(check_account_exist(username)):
		command = "SELECT password FROM accounts WHERE username = ? "
		passdb = c.execute(command, (username,)).fetchone()
		return passdb[0] == password
	return False
'''
prints_accounts
'''
def print_accounts():
	db = get_db()
	c = get_cursor(db)
	command = "SELECT * FROM accounts"
	result = c.execute(command)
	for account in result:
		print(account)
