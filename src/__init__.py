from flask import Flask, jsonify
from src.view.view import bp

app = Flask(__name__)


if __name__ == '__main__':
    app.run()
    app.register_blueprint(bp)
