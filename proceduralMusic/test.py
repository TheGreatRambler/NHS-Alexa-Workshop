import tensorflow as tf
from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('HelloIntent')
def playnote(num):
    return statement('')

if __name__ == '__main__':
    app.run(debug=True)

