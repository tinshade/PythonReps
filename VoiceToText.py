import speech_recognition as sr
import pyttsx3
from googletrans import Translator

#Speech Part
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[len(voices)-1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Recognizer Part
def recognize():
    r= sr.Recognizer()
    count = 0
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        translator = Translator()
        t = translator.translate(text, dest='hi')
        new = str(t.text)
        f = open('new.txt','w+', encoding='utf-8')
        f.write(new)
        f.close()
        return

print("Speak Now...")
recognize()