# from src import controller
import json

from .model import Model
from . import app
from flask import render_template, request
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
def front():
    return render_template('home.html')

@app.route('/main')
def main():
    return 'Main page'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    form = request.form
    company_name = form.get('company_name')
    db = Model()
    selected_list = json.loads(db.getSelectedBars(company_name))
    return render_template('choccy-frontend.html', chocolate_bars=selected_list, company=company_name)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        userName = form.username.data
        password = form.password.data
        result = Model().postUser(userName, password)

        if result == True:
            return render_template('user.html', result=result)
        else:
            return render_template('signup.html', form=form)
    else:
        return render_template('signup.html', form=form)
