import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import psutil
import pyautogui
import pyjokes
import requests, json

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('volume', 1)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!!")
        
    else:
        speak("Good Evening!!") 

    speak("I am your personal voice assistant. What can I do for you?")

def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recoginizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login({YOUR-EMAIL-ID}, {YOUR-EMAIL-PASSWORD})    #id and password
    server.sendmail({YOUT-EMAIL-ID}, to, content)
    server.close()  

def weather():
    api_key = {API-KEY} 
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")

def screenshot():
    img = pyautogui.screenshot()
    img.save("{PATH FOR THE FILE TO SAVE}")

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if ("cpu and battery" in query or "battery" in query or "cpu" in query):
            cpu()

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()
        
        elif ("weather" in query or "temperature" in query):
            weather()

        elif ("logout" in query):
            os.system("shutdown -1")
        
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")
        
        elif ('wikipedia' in query or 'what' in query or 'who' in query or 'when' in query or 'where' in query):
            speak("FINDING RESULTS FOR YOU!")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

        elif 'open insta' and 'open instagram' in query:
            speak("opening instagram!")
            print("opening instagram!")
            webbrowser.open("instagram.com")

        elif 'open youtube' in query:
            speak("opening Youtube!")
            print("opening YouTube!")
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            speak("opening facebook!")
            print("opening facebook!")
            webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            speak("opening twitter!")
            print("opening twitter!")
            webbrowser.open("twitter.com")
    
        elif 'open google' in query:
            speak("opening google!")
            print("opening google!")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak("opening facebook!")
            print("opening facebook!")
            webbrowser.open("facebook.com")

        elif 'open amazon' in query:
            speak("opening amazon!")
            print("opening amazon!")
            webbrowser.open("amazon.in")

        elif 'open github' in query:
            speak("opening Github!")
            print("opening Github!")
            webbrowser.open("github.com")
        
        elif ("tell me a joke" in query or "joke" in query):
            jokes()
            
        elif 'open stack overflow' in query:
            speak("opening Stalkoverflow!")
            print("opening Stalkoverflow!")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("Going to play music")
            print("Going to play music")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            print(strTime)
        
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'date' in query:
            speak("The current date is: ")
            speak(date)

        elif 'open python' in query:
            speak("Opening Pycharm!!")
            print("Opening Pycharm!! ")
            codePath = "{PATH OF THE FILE}"
            os.startfile(codePath)

        elif 'open codeblocks' in query:
            speak("Opening Codeblocks!!")
            print("Opening Codeblocks!!")
            codePath = "{PATH OF THE FILE}"
            os.startfile(codePath)

        elif 'open outlook' in query:
            speak("Opening Outlook!!")
            print("Opening outlook!!")
            codePath1 = "{PATH OF THE FILE}"
            os.startfile(codePath1)

        elif 'email' in query:
            try:
                speak("What shoould I say sir?")
                content = takeCommand()
                to = "{EMAIL ADDRESS WHERE YOU WANT TO SEND YOUR EMAIL}"
                sendEmail(to, content)
                speak("Email has been sent, Sir")
            except Exception as e:
                print(e)
                speak("Sorry Sir, email is not able to delivered.")

        elif 'hii' and 'you' in query:
            speak("I am good. Tell me about yourself.")
        
        elif 'good' and 'also' in query:
            speak("That's nice. Would you like me to do something for you?")

        elif ('i am done' in query or 'bye bye' in query or 'go offline' in query or 'bye' in query or 'nothing' in query):
            wishme_end()
       
