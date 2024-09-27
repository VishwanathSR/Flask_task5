from flask import Flask

app = Flask(__name__) 

@app.route('/')
def homepage ():
    return "Hello, World!"

@app.route('/about')
def login ():
    return "This is the About page."

@app.route('/goodbye')
def contact ():
    return "Goodbye, see you soon!"

app.run(debug = True)
