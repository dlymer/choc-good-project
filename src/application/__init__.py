from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'goodchoc'

from . import view, model

if __name__== '__main__':
    app.run()