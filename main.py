import speech_recognition as sr
import webbrowser
import time
from time import ctime
import pyttsx3

r = sr.Recognizer()
response = pyttsx3.init()

def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            voice_respond('Sorry, I did not get that')
            return False
        except sr.RequestError:
            voice_respond('Sorry, my speech service is down')
            return False
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        voice_respond('My name is Abhik')
    elif 'what time is it' in voice_data:
        voice_respond(ctime())
    elif 'search' in voice_data:
        voice_respond('What do you want to search for?')
        while True:
           search = record_audio() 
           if search != False:
               break
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        voice_respond('Here is what I found for ' + search)
    elif 'find location' in voice_data:
        voice_respond('What is the location?')
        location = record_audio()
        while True:
            location = record_audio()
            if location != False:
                break
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        voice_respond('Here is the location for ' + location)
    elif 'exit' in voice_data:
        voice_respond('Have a great day!')
        exit()
    else:
        voice_respond('Sorry, I do not know what to say')
    

def voice_respond(response_data):
    response.say(response_data)
    response.runAndWait()

time.sleep(1)
voice_respond('How can I help you?')
while 1:
    voice_data = record_audio()
    if voice_data:
        respond(voice_data)