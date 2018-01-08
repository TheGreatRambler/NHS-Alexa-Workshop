import random
from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

placeholderword = "--word--"

alexainterjections = ["abracadabra", "achoo", "aha", "ahem", "ahoy", "all righty", "aloha", "aooga", "argh", "arrivederci", "as you wish", "au revoir", "aw man", "baa", "bada bing bada boom", "bah humbug", "bam", "bang", "batter up", "bazinga", "beep beep", "bingo", "blah", "blarg", "blast", "boing", "bon appetit", "bonjour", "bon voyage", "boo", "boo hoo", "boom", "booya", "bravo", "bummer", "caw", "cha ching", "checkmate", "cheerio", "cheers", "cheer up", "chirp", "choo choo", "clank", "click clack", "cock a doodle doo", "coo", "cowabunga", "darn", "ding dong", "ditto", "d’oh", "dot dot dot", "duh", "dum", "dun dun dun", "dynomite", "eek", "eep", "encore", "en gard", "eureka", "fancy that", "geronimo", "giddy up", "good grief", "good luck", "good riddance", "gotcha", "great scott", "heads up", "hear hear", "hip hip hooray", "hiss", "honk", "howdy", "hurrah", "hurray", "huzzah", "jeepers creepers", "jiminy cricket", "jinx", "just kidding", "kaboom", "kablam", "kaching", "kapow", "katchow", "kazaam", "kerbam", "kerboom", "kerching", "kerchoo", "kerflop", "kerplop", "kerplunk", "kerpow", "kersplat", "kerthump", "knock knock", "le sigh", "look out", "mamma mia", "man overboard", "mazel tov", "meow", "merci", "moo", "nanu nanu", "neener neener", "no way", "now now", "oh boy", "oh brother", "oh dear", "oh my", "oh snap", "oink", "okey dokey", "oof", "ooh la la", "open sesame", "ouch", "oy", "phew", "phooey", "ping", "plop", "poof", "pop", "pow", "quack", "read ‘em and weep", "ribbit", "righto", "roger", "ruh roh", "shucks", "splash", "spoiler alert", "squee", "swish", "swoosh", "ta da", "ta ta", "tee hee", "there there", "thump", "tick tick tick", "tick-tock", "touche", "tsk tsk", "tweet", "uh huh", "uh huh", "voila", "vroom", "wahoo", "wah wah", "watch out", "way to go", "well done", "well well", "wham", "whammo", "whee", "whew", "woof", "whoops a daisy", "whoosh", "woo hoo", "wow", "wowza", "wowzer", "yadda yadda yadda", "yay", "yikes", "yippee", "yoink", "yoo hoo", "you bet", "yowza", "yowzer", "yuck", "yum", "zap", "zing", "zoinks"]

def returnrandominterjection():
    return "".join(["<say-as interpret-as='interjection'>", random.choice(alexainterjections), "</say-as>"])

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
        elif c = "k":
            returntemplate += "".join(["<amazon:effect name='whispered'>", placeholderword, "</amazon:effect>"])
        elif c = "l":
            returntemplate += "".join(["<break time='1s'/>"])  
    return "<speak>" + returntemplate + "</speak>"

@ask.launch
            
def launched():
    welcome_message = "Give me something ta rap, dawg."
    return question(welcome_message)
    
@ask.intent('RapIntent')

def rap(word):
    template = createTemplate("ababcdcdefefglglglhhhijjik").replace(placeholderword, word) + returnrandominterjection()
    return statement(template)

if __name__ == '__main__':
    app.run(debug=True)

