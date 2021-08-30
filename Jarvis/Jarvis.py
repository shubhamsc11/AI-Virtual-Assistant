import JarvisAI
import os
import re
import pprint
import random
import warnings
import tensorflow

warnings.filterwarnings("ignore")
warnings.warn("second example of warning!")

obj = JarvisAI.JarvisAssistant()


def t2s(text):
    obj.text2speech(text)


def start():
    while True:
        print("Say your AI name to activate")
        status, command = obj.hot_word_detect()
        if status:
            while True:
                # use any one of them
                print("Continue listening, say- 'stop listening to stop continue listening'")
                res = obj.mic_input()
                # res = obj.mic_input_ai(debug=True)
                print(res)

                if re.search("jokes|joke|Jokes|Joke", res):
                    joke_ = obj.tell_me_joke('en', 'neutral')
                    print(joke_)
                    t2s(joke_)

                if re.search('setup|set up', res):
                    setup = obj.setup()
                    print(setup)

                if re.search('google photos', res):
                    photos = obj.show_google_photos()
                    print(photos)

                if re.search('local photos', res):
                    photos = obj.show_me_my_images()
                    print(photos)

                if re.search('weather|temperature', res):
                    city = res.split(' ')[-1]
                    weather_res = obj.weather(city=city)
                    print(weather_res)
                    t2s(weather_res)

                if re.search('news', res):
                    news_res = obj.news()
                    pprint.pprint(news_res)
                    t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
                    t2s(news_res[0])
                    t2s(news_res[1])

                if re.search('tell me about', res):
                    topic = res[14:]
                    wiki_res = obj.tell_me(topic, sentences=1)
                    print(wiki_res)
                    t2s(wiki_res)

                if re.search('date', res):
                    date = obj.tell_me_date()
                    print(date)
                    print(t2s(date))

                if re.search('time', res):
                    time = obj.tell_me_time()
                    print(time)
                    t2s(time)

                if re.search('open', res):
                    domain = res.split(' ')[-1]
                    open_result = obj.website_opener(domain)
                    print(open_result)

                if re.search('launch', res):
                    dict_app = {
                        'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                        'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe'
                    }

                    app = res.split(' ', 1)[1]
                    path = dict_app.get(app)
                    if path is None:
                        t2s('Application path not found')
                        print('Application path not found')
                    else:
                        t2s('Launching: ' + app)
                        obj.launch_any_app(path_of_app=path)

                if re.search('hello|hi', res):
                    print('Hi')
                    t2s('Hi')

                if re.search('how are you', res):
                    li = ['good', 'fine', 'great']
                    response = random.choice(li)
                    print(f"I am {response}")
                    t2s(f"I am {response}")

                if re.search('your name|who are you', res):
                    print("I am your personal assistant")
                    t2s("I am your personal assistant")

                if re.search('what can you do', res):
                    li_commands = {
                        "open websites": "Example: 'open youtube.com",
                        "time": "Example: 'what time it is?'",
                        "date": "Example: 'what date it is?'",
                        "launch applications": "Example: 'launch chrome'",
                        "tell me": "Example: 'tell me about India'",
                        "weather": "Example: 'what weather/temperature in Mumbai?'",
                        "news": "Example: 'news for today' ",
                    }
                    ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
                    I can open websites for you, launch application and more. See the list of commands-"""
                    print(ans)
                    pprint.pprint(li_commands)
                    t2s(ans)

                if re.search("stop listening|stop", res):
                    break

        else:
            continue


if __name__ == "__main__":
    if not os.path.exists("config/config.ini"):
        res = obj.setup()
        if res:
            print("Settings Saved. Restart your Assistant")
    else:
        start()






# importing speech recognition package from google api
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
from selenium import webdriver  # to control browser operations

num = 1


def assistant_speaks(output):
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    print("PerSon : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)


def get_audio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=5)
    print("Stop.")  # limit 5 secs

    try:

        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text

    except:

        assistant_speaks("Could not understand your audio, PLease try again !")
        return 0




def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)
            return

        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Person. Your personal Assistant.
			I am here to make your life easier. You can command me to perform
			various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Shubham Singh Chouhan."
            assistant_speaks(speak)
            return

        elif "geeksforgeeks" in input:  # just
            speak = """Geeks for Geeks is the Best Online Coding Platform for learning."""
            assistant_speaks(speak)
            return

        elif "calculate" in input.lower():

            # write your wolframalpha app_id here
            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return

        elif 'open' in input:

            # another function to open
            # different application availaible
            open_application(input.lower())
            return

        else:

            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except:

        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)

def search_web(input):

	driver = webdriver.Firefox()
	driver.implicitly_wait(1)
	driver.maximize_window()

	if 'youtube' in input.lower():

		assistant_speaks("Opening in youtube")
		indx = input.lower().split().index('youtube')
		query = input.split()[indx + 1:]
		driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
		return

	elif 'wikipedia' in input.lower():

		assistant_speaks("Opening Wikipedia")
		indx = input.lower().split().index('wikipedia')
		query = input.split()[indx + 1:]
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
		return

	else:

		if 'google' in input:

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			driver.get("https://www.google.com/search?q =" + '+'.join(query))

		elif 'search' in input:

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			driver.get("https://www.google.com/search?q =" + '+'.join(query))

		else:

			driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))

		return


# function used to open application
# present inside the system.
def open_application(input):

	if "chrome" in input:
		assistant_speaks("Google Chrome")
		os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
		return

	elif "firefox" in input or "mozilla" in input:
		assistant_speaks("Opening Mozilla Firefox")
		os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
		return

	elif "word" in input:
		assistant_speaks("Opening Microsoft Word")
		os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
		return

	elif "excel" in input:
		assistant_speaks("Opening Microsoft Excel")
		os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
		return

	else:

		assistant_speaks("Application not available")
		return




# Driver Code
if __name__ == "__main__":
    assistant_speaks("What's your name, Human?")
    name = 'Human'
    name = get_audio()
    assistant_speaks("Hello, " + name + '.')

    while (1):

        assistant_speaks("What can i do for you?")
        text = get_audio().lower()

        if text == 0:
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, " + name + '.')
            break

        # calling process text to process the query
        process_text(text)



