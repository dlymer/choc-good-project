from src.controller.controller import controller
from flask import Flask, jsonify, Blueprint


bp = Blueprint('hello', __name__)

@bp.route('/')
def Test():
    print("hello world")

@bp.route('/helloworld', methods='[GET]')
def drawHelloWorld():
    return controller.renderHelloWorld()


"""if __name__== '__main__':
    app.run()"""
