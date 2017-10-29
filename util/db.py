#J.A.S.P.R.

import sqlite3
from os.path import isfile
import hashlib

path = "data/data.db"

def get_db(): #returns connection to database
	return sqlite3.connect(path)

def get_cursor(db): #returns cursor to database
	return db.cursor()

def close(db): #commits to and closes database
	db.commit()
	db.close()

#============================================================#
#============================Stories=========================#
#============================================================#

def create_story(title, text): #creates database entry for story
	db = get_db()
	c = get_cursor(db)
	ID = len(get_ids())
	cmd = "INSERT INTO stories VALUES(?, ?, ? ,?);"
	print cmd
	c.execute(cmd,(str(ID), title, '', text))
	close(db)
	return id

def get_ids(): #returns a list of all the id's
	db = get_db()
	c = get_cursor(db)
	ans = c.execute("SELECT id FROM stories;").fetchall()
	for x in range(0, len(ans)):
		ans[x] = ans[x][0]
	close(db)
	print ans
	return ans

def get_story(ID): #returns a list with title, rest_of_text, and last_text
	db = get_db()
	c = get_cursor(db)
	cmd = "SELECT title, rest_of_text, last_text FROM stories WHERE id = ?"
	text = c.execute(cmd, str(ID)).fetchone()
	ans = [text[0], text[1], text[2]]
	close(db)
	print ans
	return ans

def get_last(ID): #returns the text in the last_text
	db = get_db()
	c = get_cursor(db)
	cmd = "SELECT last_text FROM stories WHERE id = ?"
	result = c.execute(cmd, str(ID)).fetchone()
	ans = result[0]
	close(db)
	print ans
	return ans

def update_story(ID,text): #adds the given text to the story in database
	db = get_db()
	read = get_cursor(db)
	write = get_cursor(db)
	command = "SELECT rest_of_text FROM stories WHERE id = ?"
	rest_of_text = read.execute(command, str(ID)).fetchone()[0]
	command = "SELECT last_text FROM stories WHERE id = ?"
	last_text = read.execute(command, str(ID)).fetchone()[0]
	if rest_of_text == '':
		cmd = "UPDATE stories SET rest_of_text = ? WHERE id = ?"
		write.execute(cmd, (last_text, str(ID)))
	else:
		cmd = "UPDATE stories SET rest_of_text = ? WHERE id = ?"
		write.execute(cmd, (rest_of_text + "\n " +  last_text + "\n", str(ID)))
	cmd = "UPDATE stories SET last_text = ? WHERE id = ?"
	write.execute(cmd, (text + "\n", str(ID)))
	close(db)

def print_stories(): #prints all stories
	db = get_db()
	c = get_cursor(db)
	command = "SELECT * FROM stories"
	result = c.execute(command)
	for story in result:
		print story
	close(db)

#============================================================#
#============================Accounts========================#
#============================================================#
'''
if true, can display the entire story
if false, can only see the latest commit
'''
def can_view(user_id, story_id):
	db = get_db()
	c = get_cursor(db)
	stories = get_list_ac(user_id,c)
	print stories
	return story_id in stories

def get_id(username):
	db = get_db()
	c = get_cursor(db)
	command = "SELECT id FROM accounts WHERE username = ?"
	id = c.execute(command, username).fetchone()[0]
	return id

'''
grabs the list of stories from an userid
'''
def get_list_ac(user_id, c):
	data = c.execute("SELECT stories FROM accounts WHERE id = ?", str(user_id)).fetchone()
	print(data)
	list = []
	list = data[0].split(',')
    #print(len(list))
	if( list[0] != ""):
		list = map(int, list)
	return list
'''
Updates a persons stories list
CALLED AFTER EDITING A STORY
'''
def stor_list_update(user_id, story_id):
	db = get_db()
	c = get_cursor(db)
	data = c.execute("SELECT stories FROM accounts WHERE id = ?", str(user_id)).fetchone()[0]
	listo = get_list_ac(user_id, c)
	if(listo[0] == ""):
		c.execute("UPDATE accounts SET stories = ? WHERE id =" +str(user_id) , [str(story_id)])
	else:
		new = data + "," + str(story_id)
		c.execute("UPDATE accounts SET stories = ? WHERE id =" + str(user_id), [new])
	close(db)
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
	hash_object = hashlib.sha1(password)
        password = hash_object.hexdigest()
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
	print count
	return count
'''
authenticates username and password
'''
def check_account(username, password):
	db = get_db()
	c = get_cursor(db)
	hash_object = hashlib.sha1(password)
        password = hash_object.hexdigest()
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
