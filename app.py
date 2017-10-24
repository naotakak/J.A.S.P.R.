from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)

#genrerates random key
app.secret_key = os.urandom(32)

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
	

	

