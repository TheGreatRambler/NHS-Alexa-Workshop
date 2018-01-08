import random
from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
            
def launched():
    welcome_message = "Give me something ta rap, dawg."
    return statement(welcome_message)

if __name__ == '__main__':
    app.run(debug=True)
