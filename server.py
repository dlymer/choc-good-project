from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__' :
    app.run()