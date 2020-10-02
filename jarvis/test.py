import os 
import wikipedia 
import speech_recognition as sr 
import datetime
import pyttsx3
import wolframalpha
import webbrowser
import smtplib


# wolframalpha API  
YOUR_API = ""
client = wolframalpha.Client(YOUR_API)

# name 
name = "jarvis"
password = "yourpassword"

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
# setting the voice  
engine.setProperty("voice", voice[1].id)    

# all functions are starting from here 
def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def wish_me():
    # this function wishes when program is run 
    # it wishes according to time 

    hour = int(datetime.datetime.now().hour)    
    yourname = "your name"
    if hour >= 0 and hour < 6:
        print(f"Good night {yourname}! you should go to bed now ")
        speak(f"Good night {yourname}! you should go to bed now ")
    elif hour >= 6 and hour < 12:
        print(f"good morning {yourname}! ")
        speak(f"good morning {yourname}! ")
    elif hour >= 12 and hour < 18:
        print(f"good afternoon {yourname}! ")
        speak(f"good afternoon {yourname}! ")
    else:
        print(f"good evening {yourname}! ")
        speak(f"good evening {yourname} ! ")
    print("how may i help you ")
    speak("how may i help you ")

def take_command():
    # this funcdtion takes command from the user 
    # it takes microphone inputs 
    # and return string outputs 

    r = sr.Recognizer()
    # using microphone as source
    with sr.Microphone() as source:
        print("listening...")
        # pause_thershold helps us to take a small break during speaking 
        r.pause_threshold = 1 
        r.dynamic_energy_adjustment_damping = 4
        audio = r.listen(source)
    
    # well i think here i can get error so i m using try except
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("plese say that again")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("anyemail@gmail.com", password)
    server.sendmail("anyemail@gmail.com", to, content)
    server.close()
     


if __name__=="__main__":

    wish_me()
    while True:
        query = take_command().lower()
        

        # logic for execution task 

        # searching in wikipedia 
        if "wikipedia" in query:
            print("searching wikipedia...")
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences= 2)
            print(result)
            speak(f"according to wikipedia {result}")
        
        # searching in wolframe alpha (only search for temperature )
        elif "temperature" in query:
            print("searching in wolframalpha ")
            speak("searching in wolframalpha ")
            res = client.query(query)
            print(next(res.results).text)

        # youtube 
        elif "open youtube" in query:
            print("opening youtube")
            speak("opening youtube")
            webbrowser.open("youtube.com")

        # open googlw
        elif "open google" in query:
            print("opening google")
            speak("opening google")
            webbrowser.open("google.com")

        #  open stalkoverflow
        elif "open stalkoverflow" in query:
            print("opening stalkoverflow")
            speak("opening stalkoverflow")
            webbrowser.open("stalkoverflow.com")

        elif "play music" in query:
            music = "D:\\songs"
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"the time is {strTime}")
            speak(f"the time is {strTime}")
        
        elif "open code" in query:
            CodePath = "C:\\Users\\debakrishna\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening visual studio code")
            os.startfile(CodePath)
        
        elif "your name" in query:
            print(f"my name is {name}")
            speak(f"my name is {name}")

        elif "love me" in query:
            speak("yes i love you always")


        # email send  
        elif "send email" in query:
            try:
                speak("what should i say")
                content = take_command()
                to = "anyemail@gmail.com"
                sendEmail(to, content) 
                speak("email has beenn sent ")
            except Exception as e:
                print(e)
                speak("email not sent due to some error")

        elif "quit" in query:
            speak("i am sad you are leaving")
            speak("thank you for your time")
            speak("byeeee")
            exit()