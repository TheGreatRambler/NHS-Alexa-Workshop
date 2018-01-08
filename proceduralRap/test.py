import tensorflow as tf
from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

placeholderword = "--word--"

@ask.intent('RapIntent')

def createTemplate(raptemplate):
    returntemplate = ""
    for c in raptemplate:
        if c = "a":
            returntemplate += "".join(["<prosody pitch='x-high'>", placeholderword, "</prosody>"])
        elif c = "b":
            returntemplate += "".join(["<prosody pitch='high'>", placeholderword, "</prosody>"])
        elif c = "c":
            returntemplate += "".join(["<prosody pitch='medium'>", placeholderword, "</prosody>"])
        elif c = "d":
            returntemplate += "".join(["<prosody pitch='low'>", placeholderword, "</prosody>"])
        elif c = "e":
            returntemplate += "".join(["<prosody pitch='x-low'>", placeholderword, "</prosody>"])
        elif c = "f":
            returntemplate += "".join(["<prosody rate='x-fast'>", placeholderword, "</prosody>"])
        elif c = "g":
            returntemplate += "".join(["<prosody rate='fast'>", placeholderword, "</prosody>"])
        elif c = "h":
            returntemplate += "".join(["<prosody rate='medium'>", placeholderword, "</prosody>"])
        elif c = "i":
            returntemplate += "".join(["<prosody rate='slow'>", placeholderword, "</prosody>"])
        elif c = "j":
            returntemplate += "".join(["<prosody rate='x-slow'>", placeholderword, "</prosody>"])
    return returntemplate;
            
def rap(word):
    template = createTemplate("ababcdcdefefggghhhijji").replace(placeholderword, word)
    return statement(template)

if __name__ == '__main__':
    app.run(debug=True)

