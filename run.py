# Import os and Flask
import os
from flask import Flask, redirect

# Initialize the Flask application 
app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the `messages` list"""
    messages.append("{}: {}".format(username, message))

def get_all_messages():
    """Get all of the messages and separate them with a `br`"""
    return "<br>".join(messages)


# Setting the App route decorator / Where to start our App from
@app.route('/') # The route is set with ('/') since this is the only text after the domain-name.com in the url.
# Define my variable of the index page 
def index():
    # Returing how to send a message
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

# A app route for the username
@app.route('/<username>')
# New def function for username and what it will return
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())

# A App route for sending messages.
@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

# App run is setup with Heroku. To use the shorthand code you need to use "getenv() in your host and port, this is an 
# environment variable set in Gitpod. See the Thorin and Company project for longhand code"
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)