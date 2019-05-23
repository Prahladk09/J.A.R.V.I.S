import datetime
import sys
import pyttsx3
import speech_recognition as sr
import wikipedia
import googlesearch
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1] .id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("How may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir you said: {query}\n")
        speak(f"sir you said: {query}")

    except Exception as e:
        print("I did't get. Please say it again...")
        speak("I did't get. Please say it again...")
        return "none"
    return query



if __name__ == '__main__':
    wishMe()
    while True:
    #if 1:
        query = takecommand().lower()
        #logic for executing tasks based on input query

        if 'wikipedia' in query:
            speak('Searching on wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        if 'google' in query:
            speak('Searching on google...')
            query = query.replace("google", "")
            results = googlesearch.summary(query, sentences=2)
            speak("According to google")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening sir")
            webbrowser.open("youtube.com")
        #elif 'open google' in query:
         #   webbrowser.open("google.com")
        elif 'open gmail' in query:
            speak("opening sir")
            webbrowser.open("gmail.com")
        elif 'open stakoverflow' in query:
            speak("opening sir")
            webbrowser.open("stackoverflow.com")
        elif 'open github' in query:
            speak("opening sir")
            webbrowser.open("github.com")

        elif 'play song' or 'play music' or 'play songs' in query:
            music_dir = 'F:\\Songs'
            songs = os.listdir(music_dir)
            print("Playing song for you sir")
            speak("Playing song for you sir")
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open pycharm' in query:
            charmPath = "C:\\Program Files\\JetBrains\\PyCharm 2019.1.2\\bin\\pycharm64.exe"
            speak("opening sir")
            os.startfile(charmPath)


        elif 'quit' or 'exit' or 'nothing' in query:
            speak("ok! bye sir have a nice day")
            sys.exit()

