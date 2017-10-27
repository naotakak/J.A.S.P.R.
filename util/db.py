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
	db = sqlite3.connect("data.db")
	c = db.cursor()
	stories = get_list_ac(user_id,c)
	return story_id in stories


def get_list_ac(user_id, c):
	data = c.execute("SELECT stories FROM accounts WHERE id = ?", user_id)
	list = []
	list = data[0].spilt(',')
	list = map(int, list)


def check_account_exist(username):
	db = get_db()
	c = get_cursor(db)
	command = "SELECT username FROM accounts WHERE username = \"" + username + "\""
	usernames = c.execute(command)
	for list_username in usernames:
		return list_username != None
	return False

def create_account(username, password):
	db = get_db()
	c = get_cursor(db)
	command = "INSERT INTO accounts VALUES (\"" + username + "\", \"" + password + "\"," + "\"\"" + ", " + str(new_ac_id()) + " )"
	print command
	c.execute(command)
	close(db)

def new_ac_id():
	db = get_db()
	c = get_cursor(db)
	command = "SELECT COUNT(*) FROM accounts"
	result = c.execute(command)
	for count in result:
		print count
		return count[0]


def check_account(username, password):
	db = get_db()
	c = get_cursor(db)
	if(check_account_exist(username)):
		command = "SELECT password FROM accounts WHERE username = ? "
		passdbs = c.execute(command, (username,))
		for passdb in passdbs:
			return passdb[0] == password
	return False
