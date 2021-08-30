import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

# other libraries
import city
import ctypes
import pyjokes
import smtplib
from email.message import EmailMessage



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #here value can be 0 or 1.

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:

        print('Hello, Good Morning')
        speak('Hello, Good Morning')


    elif hour>=12 and hour<18:

        print('Hello, Good Afternoon')
        speak('Hello, Good Afternoon')

    else:

        print('Hello, Good Evening')
        speak('Hello, Good Evening')

# wishMe()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        statement = r.recognize_google(audio, language='en-in')
        print(f"User said: {statement}\n")

    except Exception as e:
        print('say that again please...')
        speak('say that again please...')
        return "None"
    return statement

print("Loading your AI persoanl assistant My-Assistant001")
speak("Loading your AI persoanl assistant My-Assistant001")
wishMe()


if __name__ == '__main__':

    while True:
        print("Tell me how can I help you sir?")
        speak("Tell me how can I help you sir?")
        statement = takecommand().lower()

        if statement == 0:
            continue


        # 1. Fatching data from Wikipedia
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        # 2. Accessing the Web Browsers — Google chrome , G-Mail, Facebook and YouTube

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            print("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            print("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            print("Google Mail open now")
            time.sleep(5)

        elif 'open facebook' in statement:
            webbrowser.open_new_tab("facebook.com")
            speak('facebook is open now')
            print('facebook is open now')
            time.sleep(5)


        # 3. Predicting time
        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")



        # 4. To fetch latest news
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)


        # 5. Capturing photo

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "jarvis camera", "img.jpg")


        # 6. Searching data from web

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        # 7. Setting your AI assistant to answer geographical and computational questions

        elif 'ask' in statement or 'find' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            print('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = takecommand()
            app_id = "K9PU3W-439VPGYUQU " # wolframalpha account unique app id paste here.
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)


        # 8. To forecast weather

        elif "weather" in statement:
            api_key = "K9PU3W-439VPGYUQU"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takecommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"]!="404":
                y = x['main']
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))


        # 9. Calculator
        elif 'calculate' in statement.lower():
            app_id = "K9PU3W-439VPGYUQU"
            clint = wolframalpha.Client(app_id)
            indx = statement.lower().split().index('calculate')
            query = statement.split()[indx + 1:]
            res = clint.query(' '.join(query))
            answer = next(res.results).txt
            print('the answer is' + answer)
            speak('the answer is' + answer)



        # 10. Write & Show notes
        elif "write a note" in statement:
            speak("What should i write, sir")
            note = takecommand()
            file = open('data.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show notes" in statement:
            speak("Showing Notes")
            file = open("data.txt", "r")
            print(file.read(6))
            speak(file.read(6))


        # 11. basic daily routine questions

        elif 'how are you' in statement:
            speak("I am fine. Thank You")
            print("I am fine. Thank You")
            speak("How are you sir?")

        elif 'good' in statement or 'fine' in statement:
            speak("its good to know that you are fine")
            print("its good to know that you are fine")

        elif 'who are you' in statement or "define yourself" in statement:
            print('''Hello, I am your personal assistant. My name is My-Assistant001. My technology is a 
            based on artificial intelligence. And my latest version is 0.0.1 . I am here to make your life easier. 
            You can command me to perform various tasks such as calculating sums, opening applications and search
             anything in a second's etcetra.''')

            speak('''Hello, I am your personal assistant. My name is My-Assistant001. My technology is a 
            based on artificial intelligence. And my latest version is 0.0.1 . I am here to make your life easier. 
            You can command me to perform various tasks such as calculating sums, opening applications and search
             anything in a second's etcetra.''')


        elif "who made you" in statement or "who created you" in statement:
            print("I have been created by The Computer Science Engineer - Mister Shubham Singh Chouhan.")
            speak("I have been created by The Computer Science Engineer - Mister Shubham Singh Chouhan.")




        # 12. basic operations on system
        elif 'lock windows' in statement:
            speak("locking windows")
            ctypes.windll.user32.lockWorkStation()

        elif 'shutdown windows' in statement:
            speak("shutting down windows")
            subprocess.call('shutdown / p /f')

        elif 'hibernate windows' in statement:
            speak("hibernating windows")
            subprocess.call('shutdown / h')

        elif 'restart' in statement:
            subprocess.call(["shutdown", "/r"])


        # 13. Some Another operations like play music, send mail, & listen jokes

        elif 'play music' in statement or "play song" in statement:
            speak("Here you go with music")
            print("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "E:\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[0]))


        elif 'send mail to friend' in statement:
            try:
                msg = EmailMessage()
                msg['Subject'] = "Check out new mail"
                msg['From'] = 'sender mail'
                msg['To'] = 'receiver mail'
                msg.set_content('Hello, My dear friend! How are you? ')
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this email")


        elif 'jokes' in statement:
            joke = speak(pyjokes.get_joke())
            print(joke)


        #13. Open any application
        elif "open sublime" in statement or "open sublime text" in statement:
            speak("Here, you go to sublime text")
            print("Here, you go to sublime text")
            codepath = "path here"
            os.startfile(codepath)

        elif "open word" in statement or "open msword" in statement:
            speak("Opening Microsoft Word")
            print("Opening Microsoft Word")
            codepath = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft Office Word 2007"
            os.startfile(codepath)

        elif "open excel" in statement or "open msexcel" in statement:
            speak("Opening Microsoft Excel")
            print("Opening Microsoft Excel")
            codepath = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/Microsoft Office Excel 2007"
            os.startfile(codepath)

        # else:
        #     speak("Application not available")
        #     print("Application not available")
        #     return



        # 14. ok bye assistant
        elif "good bye" in statement or "ok bye" in statement or "stop" in statement:

            print("Your personal assistant My-Assistant001 is shutting down, Good bye")
            speak("Your personal assistant My-Assistant001 is shutting down, Good bye")

            break


        # 15. To log off your PC
        elif "log off" in statement or "sign out" in statement:
             speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
             subprocess.call(["shutdown", "/l"])

    time.sleep(3)










