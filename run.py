# Import os and Flask
import os
from flask import Flask

# Initialize the Flask application 
app = Flask(__name__)

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
    return "Hi " + username

@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)

# App run is setup with Heroku. To use the shorthand code you need to use "getenv() in your host and port, this is an 
# environment variable set in Gitpod. See the Thorin and Company project for longhand code"
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)