import playsound
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
# import _json
# import requests
# import wolframalpha
from gtts import gTTS

# from JARVIS.Assistant import get_audio, search_web, open_application

num = 1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # print(voices[1].id) engine.setProperty​('voice', voices[0].id)


def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        speak("Good Morning sir!")

    elif (hour >= 12) and (hour < 18):
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I am Jarvis. Please tell me how may I help you")



def takecommand():  # It takes microphone input from the user and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  # print(e)

        print("Say that again please...")
        return "None"
    return query

# for voice change


def assistant_speaks(output):
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    print("PerSon : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = "{0}.mp3".format(str(num))
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)


if __name__ == "__main__":

    wishme()
    while True:  # if 1:

        query = takecommand().lower()    # Logic for executing tasks based on query

# Wikipedia Search

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


# Open Application

        elif "chrome" in query:
            speak("Opening Chrome ")
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')


        elif "xyz" in query:
            speak("Opening Microsoft Edge")
            os.startfile('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')



# Open Web Application

        elif 'youtube' in query:
            speak(f"Opening youtube")
            webbrowser.open("​www.youtube.com​")


        elif 'google' in query:
            speak(f"Opening Google")
            webbrowser.open("​www.google.com​")

# Desktop Application Open image and Play Song

        elif 'music' in query:
            speak(f"Play Music")
            music_dir = 'J:\SONGS\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'image' in query:
            speak(f"Opening image")
            image_dir = 'J:\PHOTOS\JAY\pro'
            image = os.listdir(image_dir)
            print(image)
            os.startfile(os.path.join(image_dir, image[0]))

        elif 'pdf' in query:
            speak(f"Opening pdf")
            dir = 'F:\CE\SEM 7\Project'
            pd = os.listdir(dir)
            print(pd)
            os.startfile(os.path.join(dir, pd[1]))

# Time
        elif 'the time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


# Assistant self

        elif "define yourself" in query:

            speak(f" Hello Sir, I am Your personal Assistant. I am here to make your life easier. You can command me "
                  f"to perform various tasks such as opening applications or play music etcetra")

        elif "who made you" in query or "created you" in query:
            speak(f"I have been created by Faculty and Project team.")

# Exit

        elif "exit" in query:
            speak(f"Ok goodbye Sir, Have a Good Day ")
            break








