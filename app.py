from flask import Flask, render_template, redirect, url_for, request, session
from util import db
import os

app = Flask(__name__)

#genrerates random key
app.secret_key = os.urandom(32)

def checklogged():
    if session.has_key('username'): #renders welcome page if a 'username' key exists
        return redirect(url_for('home')) #tells the user they are logged in
    return render_template('login.html') #otherwise renders the login page

def addToSession(username):
    session['username'] = username

@app.route("/")
def root():
	return checklogged()

@app.route("/home")
def home():
	return "HOME"

@app.route("/display_create")
def display_create():
    return render_template("account.html")

@app.route("/auth", methods = ['POST'])
def login():
    username = request.form["User"]
    password = request.form["Pass"]
    if db.check_account(username, password):
        addToSession(username)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('display_create'))

@app.route("/create_account", methods = ['POST'])
def create_account():
    username =  request.form["NUser"]
    password = request.form["NPass"]
    addToSession(username)
    if not db.check_account_exist(username):
        print "Hello"
        db.create_account(username, password)
    else:
        return redirect(url_for('display_create'))
    return redirect(url_for('home'))

@app.route("/view_contr_stories")
def view_contr_stories():
	return

@app.route("/story")
def view_story():
	return render_template("story.html")

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
