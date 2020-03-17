# Import os and Flask
import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

# Initialize the Flask application 
app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_message(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})


# Setting the App route decorator / Where to start our App from
@app.route('/', methods = ["GET", "POST"]) # The route is set with ('/') since this is the only text after the domain-name.com in the url.
# Define my variable of the index page 
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))


    return render_template("index.html")

# A app route for the username
@app.route('/chat/<username>', methods = ["GET", "POST"])
# New def function for username and what it will return
def user(username):
    """Add and display chat messages"""

    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))

    return render_template("chat.html", username = username, chat_messages = messages)

# App run is setup with Heroku. To use the shorthand code you need to use "getenv() in your host and port, this is an 
# environment variable set in Gitpod. See the Thorin and Company project for longhand code"
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)