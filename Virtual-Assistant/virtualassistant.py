import webbrowser

import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr # pip install speechRecognition
import wikipedia # pip install wikipedia
import webbrowser
import webbrowser as wb
import os
import smtplib
import pyjokes #pip install pyjokes
import subprocess
import ctypes #pip install ctypes
import winshell #pip install winshell
import wolframalpha
import json
import win32com.client as wincl
import time
import requests
import ecapture as ec #pip install ecapture


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)#here value can be 0 or 1.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak('Good Morning')

    elif hour>=12 and hour<18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('I am your personal assistant sir. please tell me how may i help you.')

# wishMe()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print('say that again please...')
        speak('say that again please...')
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremailaddress', 'password')
    server.sendmail('email id', to, content)
    server.close()


if __name__=='__main__':
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'search in chrome' in query:
            speak('what should i search?')
            chromepath = "path here"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.open("facebook.com")


        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "E:\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[0]))

        elif 'send mail to friend' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "friends mail address"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this email")

        elif "open sublime" in query:
            speak("here you go to sublime")
            codepath = "path here"
            os.startfile(codepath)

        elif 'jokes' in query:
            speak(pyjokes.get_joke())

            #basic questions

        elif 'how are you' in query:
            speak("I am fine. Thank You")
            print("I am fine. Thank You")
            speak("How are you sir")

        elif 'good' in query:
            speak(" its good to know that you are fine")

        elif 'who are you' in query:
            speak(" i am your personal assistant")

            #amoazon alexa or google assistant ke basic question search.

            #subprocesses

        elif 'lock windows' in query:
            speak("locking windows")
            ctypes.windll.user32.lockWorkStation()

        elif 'shutdown windows' in query:
            speak("shutting down windows")
            subprocess.call('shutdown / p /f')

        elif 'hibernate windows' in query:
            speak("hibernating windows")
            subprocess.call('shutdown / h')

        elif 'restart' in query:
            subprocess.call(["shutdown", "/r"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('data.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("data.txt", "r")
            print(file.read())
            speak(file.read(6))


        elif 'news' in query:

            try:
                jsonObj = urlopen("https://newsapi.org/v2/everything?q=apple&from=2021-07-18&to=2021-07-18&sortBy=popularity&apiKey=b44a88af98644a0fa53ba0c783175153")
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif 'find' in query:
            app_id = "K9PU3W-439VPGYUQU"
            clint = wolframalpha.Client(app_id)
            indx = query.lower().split().index('find')
            query = query.split()[indx + 1:1]
            res = clint.query(''.join(query))
            answer = next(res.results).txt
            print('the answer is' + answer)
            speak('the answer is' + answer)


        elif 'calculate' in query:
            app_id = "K9PU3W-439VPGYUQU"
            clint = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:1]
            res = clint.query(''.join(query))
            answer = next(res.results).txt
            print('the answer is' + answer)
            speak('the answer is' + answer)

        elif 'take a photo' in query:
            ec.ecapture(0, "jarvis camera ", "img.jpg")

        elif "the time" in query:
            strTime = datetime.date.strftime("%h:%m:%s")
            speak(f"sir, the time is", strTime)













