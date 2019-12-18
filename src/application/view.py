#from src import controller
from .model import Model
from . import app
from flask import render_template

db = None

def init_view(db):
    db = db

@app.route('/helloworld', methods=["GET"])
def drawHelloWorld():
    return db.getHelloWorld()


@app.route('/hellohtml')
def drawhellohtml():
    db = Model()
    return render_template('hello.html', message=db.getHelloWorld())

#@app.route()