# from src import controller
import json

from .model import Model
from . import app
from flask import render_template
from .forms import SignUpForm



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
    chocolate_bar_dict = json.loads(db.get_ChocolateBars())
    return render_template('choccy-frontend.html', chocolate_bars=chocolate_bar_dict)


@app.route('/')
def home():
    return 'Chocolatey Goodness homepage'


@app.route('/main')
def main():
    return 'Main page'


@app.route('/search')
def search():
    return render_template('choccy-frontend.html', company="Cadbury's")


@app.route('/about')
def about():
    return 'About us'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = Model().post()
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)
