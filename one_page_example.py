from flask import Flask

app = Flask(__name__)

@app.route('/')
def land():
    return {
        "you've officially landed!" : "Welcome young Padawans to Flask!"
    }

app.run()

@app.route('/bridge')
def bridge():
    return {
        "the bridge welcome"
    }

app.run()

@app.route('/barracks')
def barracks():
    return {
        "this is the barracks you will spend most of your time here"
    }

app.run()

@app.route('/armory')
def armory():
    return {
        "the good stuff"
    }

app.run()

@app.route('/brigg')
def brigg():
    return {
        "the place for the bad guys"
    }

app.run()

