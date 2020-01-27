""" File contains the a simple Flask instance """

__version__ = '0.1 (2020-01-26)'
__author__ = 'OSAHON OKUNGBOWA'

from flask import Flask # import the Flask module 

app = Flask(__name__) # create Flask app instance

# DEFINE ROUTES
@app.route('/')
def index(): # define index route
    return "HELLO WORLD FROM ME TO YOU!!"



# START THE SERVER PROGRAMMATICALLY
if __name__ == "__main__": # if this module is being executed as the "main" module
    app.run(debug=True) # run the server (in debug mode)