from src.controller.controller import controller
from src import app
from flask import render_template


@app.route('/helloworld', methods=["GET"])
def drawHelloWorld():
    return controller.renderHelloWorld()


@app.route('/hellohtml')
def drawhellohtml():
    return render_template('hello.html', message=controller.renderHelloWorld())
