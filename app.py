from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)

#genrerates random key
app.secret_key = os.urandom(32)

'''
if true, can display the entire story
if false, can only see the latest commit
def can_view(user_id, story_id):
	stories = db.get_list(user_id)
	return story_id in stories 
'''

'''
#Accounts database Functions
def check_account(username):
	command = "SELECT username FROM accounts"
	usernames = c.execute(command)
	for list_username in usernames:
		if list_username == username:
			return False
	return True
	
def create_account(username, password):
	command = "INSERT INTO accounts VALUES (" + username + ", " + password + ")" 
'''


@app.route("/")
def root():
	return "hi" 

@app.route("/home")
def home():
	return

@app.route("/login")
def login():
	return
	
@app.route("/create_account")
def create_account():
	return
	
@app.route("/view_contr_stories")
def view_contr_stories():
	return

#could be /edit only
@app.route("/create_story")
def create_story():
	return
	
@app.route("/index_stories")
def index_stories():
	return
	
@app.route("/edit")
def edit_story():
	return

	
if __name__ == '__main__':
    app.debug = True
    app.run()
	

	

