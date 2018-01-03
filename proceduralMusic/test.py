import tensorflow as tf
from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

mp3rootname = "something"

@ask.intent('HelloIntent')
def playnote(notename):
    return statement("<speak><audio src=" + mp3rootname + notename + ".mp3" /></speak>")

if __name__ == '__main__':
    app.run(debug=True)

