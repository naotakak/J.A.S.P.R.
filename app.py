from flask import Flask, render_template, redirect, url_for, request, session, flash
from util import db
import os

app = Flask(__name__)

#genrerates random key
app.secret_key = os.urandom(32)

def logged():
    return session.has_key('username')

def addToSession(username):
    session['username'] = username
    session['ID'] = db.get_id(username)

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

'''
Displays All Stories
'''
@app.route("/home")
def home():
    print("***HOME***\n")
    if not logged():
        return redirect(url_for('root'))
    stories_ids = db.get_ids()
    stories_dict = {}
    for id in stories_ids:
        story = db.get_story(id)
        link = ""
        #LINK NEEDS TO CHANGE DEPENING ON IF USER CAN VIEW
        stories_dict[id] = [story[0], story[1] + " " + story[2]]
    print stories_dict
    return render_template('home.html', stories = stories_dict)

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
            flash("*Incorrect Username/password*")
            return redirect(url_for('root'))
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
        db.create_account(username, password)
        addToSession(username)
    else:
        print "Username not Available"
        flash("Username Not Available")
    return redirect(url_for('home'))

'''
Displays A Story
/story/<int:story_id> allows us to
display a specific story
'''
@app.route("/story/<int:story_id>")
def view_story(story_id):
    if not logged():
        return redirect(url_for('root'))
    print "***VIEW STORY***\n"
    print "Story Id: " + str(story_id)
    story = db.get_story(story_id)
    title = story[0]
    text = story[1] + " " + story[2]
    return render_template("story.html", title = title, story = text)

'''
Allows User to edit a story
'''
@app.route("/edit/<int:story_id>", methods = ["GET", "POST"])
def edit_story(story_id):
    if not logged():
        return redirect(url_for('root'))
    print "***EDIT***\n"
    print "Story Id: " + str(story_id)
    if request.method == "POST":
        print "updating story..."
        new_text = request.form["addition"]
        db.update_story(story_id, new_text)
        #Once we've Edited, display it
        return redirect("/story/" + str(story_id))
    story = db.get_story(story_id)
    title = story[0]
    text = story[2]
    return render_template("edit.html", title = title, story = text, story_id=story_id)


@app.route("/logout")
def logout():
    print "***LOG OUT***"
    if logged():
        session.pop('username')
    return redirect(url_for("root"))


if __name__ == '__main__':
    app.debug = True
    app.run()
