"""
Hello world flask app
"""
from flask import Flask, jsonify
from modules import service_now

app = Flask(__name__)


@app.route('/')
def hello_word():
    obj = service_now.Adapater("https://www.booknomads.com")
    return jsonify(obj.get_books())
