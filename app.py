from flask import Flask, render_template, redirect, url_for, request, session
import util
import os

app = Flask(__name__)
#db = util.get_db()
#c = util.get_cursor(db)

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
    username = request.form["Nuser"]
    password = request.form["NPass"]
	#if check_account(request.form['User'], request.form['Pass']):
    if (True):
        addToSession(username)
        return redirect(url_for('home'))
    else:
        flash('Your Username/Password was incorrect!')

@app.route("/create_account", methods = ['POST'])
def create_account():
    username =  request.form["Nuser"]
    password = request.form["NPass"]
    addToSession(username)
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
