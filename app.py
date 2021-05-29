import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import requests
import json
import time
from win10toast import ToastNotifier

Alax=pyttsx3.init()
voices=Alax.getProperty('voices')
Alax.setProperty('voice', voices[0].id)
name = ""

def speak(audio):
    print('Alax: ' + audio)
    Alax.say(audio)
    Alax.runAndWait()

def time():
    Time=datetime.datetime.now().strftime('%I:%M:%p')
    speak(f"Now is: {Time}")

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'Cases : {data["cases"]} \nDeath : {data["deaths"]} \nRecovered : {data["recovered"]}'
    t = ToastNotifier()
    speak(f"Look at the announcement, here's the world's covid patient data")
    t.show_toast("Covid 19 Update", text, icon_path="icon.ico", duration=20)
    speak(f"The epidemic situation is very complicated, please follow the 5k rule of the Ministry of Health")

def webcome():
    global name
    hour=datetime.datetime.now().hour
    if hour > 6 & hour < 12:
        speak('Good morning sir!')
    elif hour > 12 & hour < 18:
        speak('Good Afternoon sir')
    elif hour >=18 & hour <= 24:
        speak('Good night sir')
    speak('How i can call you, sir ... ')
    name = str(input('Your name: '))
    speak(f'How i can help your, {name} !')

def sendMessage():
    # https://fbchat.readthedocs.io/en/stable/
    pass

def messZalo():
    # https://developers.zalo.me/docs/api/social-api-4
    pass

def command():
    c=sr.Recognizer()
    with sr.Microphone() as mic:
        c.pause_threshold=2
        audio = c.listen(mic)
    try:
        query = c.recognize_google(audio, language='en-US')
        print(f'{name}: ' + query)
    except sr.UnknownValueError:
        print('Sorry')
        query = str(input('Your mean is: '))
    return query

if __name__ == '__main__':
    webcome()    
    while True:
        query=command().lower()
        if "google" in query:
            speak(f"What should I search, {name}")
            search=command().lower()
            url=f"https://google.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f"Here is your {search} on Google")

        elif "youtube" in query:
            speak(f"What should I search, {name}")
            search=command().lower()
            url=f"https://youtube.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f"Here is your {search} on youtube")

        elif "spotify" in query:
            spotify=r"C:\Users\Admin\AppData\Roaming\Spotify\Spotify.exe"
            os.startfile(spotify)    

        elif "music" in query:
            speak("Open music form Spotify, let enjoy it")
            url=r"https://open.spotify.com/playlist/37i9dQZF1E36CKuUvp8aGt?si=397f9de5bb3d4483"
            webbrowser.get().open(url)

        elif "covid" in query:
            covid()

        elif "send message" in query:
            sendMessage()

        elif "zalo" in query:
            messZalo()

        elif "time" in query:
            time()

        elif "bye" in query:
            speak(f"Goodbye {name}, see you soon")
            quit()        
          