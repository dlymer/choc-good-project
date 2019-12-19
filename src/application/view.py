#from src import controller
from .model import Model
from . import app
from flask import render_template


@app.route('/helloworld', methods=["GET"])
def drawHelloWorld():
    db = Model()
    return db.getHelloWorld()


@app.route('/hellohtml')
def drawhellohtml():
    db = Model()
    return render_template('hello.html', message=db.getHelloWorld())

@app.route('/choccy-frontend')
def display_choccy_bars():
    db = Model()
    chocolate_bar_list = db.get_ChocolateBars()
    return render_template('choccy-frontend.html', chocolate_bars=chocolate_bar_list)
