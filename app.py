from flask import Flask, render_template, redirect, url_for, request, session
from util import db
import os

app = Flask(__name__)

#genrerates random key
app.secret_key = os.urandom(32)

def logged():
    return session.has_key('username')

def addToSession(username):
    session['username'] = username

@app.route("/")
def root():
    print("\n***ROOT***\n")
    print "Accounts: \n"
    db.print_accounts()
    print "\nStories: \n"
    db.print_stories()
    if logged():
        print("User Logged in, redirecting to home")
        return redirect(url_for('home'))
    else:
        print("User not logged in, redirecting to login")
        return render_template('login.html')

@app.route("/home")
def home():
    print("***HOME***\n")
    if not logged():
        return redirect(url_for('root'))
    dbstory = db.get_story(0)
    if dbstory == '':
        return render_template('story.html', title = dbstory[0], story = dbstory[2])
    return render_template('story.html', title = dbstory[0], story = dbstory[1] + " " + dbstory[2])

'''
If the user is trying to login, take the username
and Password they inputted and send them to the database functions
that check if their account exists
If the user is trying to create an acocunt, redirect them to /create_account
'''
@app.route("/auth", methods = ['POST', 'GET'])
def login():
    print("***LOGIN***\n")
    #User Pressed Login Button
    if request.method == 'POST':
        username = request.form["User"]
        password = request.form["Pass"]
        print("Inputted:\n Username: " + username + "\n Password: "+ password + "\n")
        if db.check_account(username, password):
            addToSession(username)
            print("User Logged in")
            return redirect(url_for('home'))
        else:
            print("Incorrect Username and password")
            return redirect(url_for('root'))
            #flash(error)
    #User Pressed Create Account Button
    elif request.method == 'GET':
        print("User wants to create account\n")
        return render_template('account.html')

'''
Take the user's inputted username and password
and send them to the database functions that will add them to the database
'''
@app.route("/create_account", methods = ['POST'])
def create_account():
    print("***Create Account***\n")
    username =  request.form["NUser"]
    password = request.form["NPass"]
    print("Inputted:\n Username: " + username + "\n Password: "+ password + "\n")
    #log them in
    if not db.check_account_exist(username):
        print "Username Available, making account..."
        addToSession(username)
        db.create_account(username, password)
    else:
        print "Username not Available"
        #flash
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

@app.route("/logout")
def logout():
    if logged():
        session.pop('username')
    return redirect(url_for("root"))


if __name__ == '__main__':
    app.debug = True
    app.run()
