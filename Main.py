import speech_recognition as sr
import webbrowser
import pyttsx3
import requests

newsapi = ""  # Ensure to use your valid API key here
# INSTEAD USE THIS: newsapi="get your own api key"

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "news" in c.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                if articles:
                    for article in articles:
                        speak(article['title'])
                else:
                    speak("No articles found.")
            else:
                speak("Sorry, there was an error retrieving the news.")
        except requests.exceptions.RequestException as e:
            speak("There was a problem fetching the news.")
            print(f"Error: {e}")
    else:
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        print("Listening...")
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes, how can I assist you?")
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print(f"Error: {e}")