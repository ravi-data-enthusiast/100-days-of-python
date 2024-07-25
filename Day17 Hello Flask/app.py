#render_template is responsible for redirecting to that particular page.
from flask import Flask, render_template
''' 
It creates an instance of the flask class, which will be your WSGI(Web server
gate way interface)application.
'''
###WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to flask application by ravi..</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

#The below line means, the execution starts from here
if __name__ == "__main__":
    #runs the entire flask() application, debug parameter, helps to restart server on its own after saving.
    app.run(debug=True)

