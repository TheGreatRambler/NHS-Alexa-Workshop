from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

noteletter = "a"

# songspeeds greater than 100 are faster and less than 100 are slower: 20 is the minimum speed
songspeed = 150

def returnnote(pitch, duration):
    transformedpitch = ""
    if pitch < 30:
        num = str(pitch + 30)
        transformedpitch = "-" + num + "%"
    elif pitch > 30:
        num = str(pitch - 30)
        transformedpitch = "+" + num + "%"
    elif pitch == 30:
        transformedpitch = "+0%"
    return "<prosody pitch='" + transformedpitch + "' rate='" + str(duration) + "%'>" + noteletter + "</prosody>"

@ask.launch
            
def launched():
    song = ""
    for x in range(0, 8):
         song += returnnote(x * 10, songspeed)
    music = "<speak>" + song + "</speak>"
    return statement(music)

if __name__ == '__main__':
    app.run(debug=True)
