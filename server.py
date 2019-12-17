from flask import Flask, render_template, redirect, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'goodchoc'

@app.route('/')
def home():
    return 'Chocolatey Goodness homepage'

@app.route('/main')
def main():
    return 'Main page'

@app.route('/search')
def search():
    return render_template('choccy-frontend.html', company = "Cadbury's")

@app.route('/about')
def about():
    return 'About us'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result=request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

if __name__ == '__main__' :
    app.run()