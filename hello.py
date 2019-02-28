from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def hello_word():
    return 'hello world'
