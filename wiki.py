import wikipedia
import pyttsx3
from prettytable import PrettyTable

engine = pyttsx3.init()
engine.say("What do you want to know:")
engine.runAndWait()
a=input("What do you want to know:")
try:
    s=(wikipedia.summary(str(a),sentences=3))
    x = PrettyTable()
    x.field_names = [str(a)]
    x.add_row(["**********Information**********"])
    print(x.get_string(fields=[str(a)]))
    print(str(s))
    engine.say(str(s))
    engine.runAndWait()
    
except:
    e="Sorry We cant find Information"
    print(str(e))
    engine.say(str(e))
    engine.runAndWait()