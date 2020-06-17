import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    h=int(datetime.datetime.now().hour)
    if(h>=0 and h<=12):
        temp="Good Morning Dear"
    elif(h>12 and h<=18):
        temp="Good Afternoon Dear"
    else:
        temp="Good Evening Dear"
    print(temp)
    speak(temp)    
    print("I am JARVIS. Tell me how may i help you?")
    speak("I am JARVIS. Tell me how may i help you?")

def takecommand():
    '''Insert A Docstring-It takes microphone input from the user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language='en-in')
        #print(f"User Said : {query}")
        #speak(f"You Said {query}")
    except Exception as e:
        print(e)
        print("Say That Again Please.....")
        return("None")
    return query

def send_email(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("email@gmail.com","******")
    server.sendmail("email@gmail.com",to,content)
    server.close()
if __name__ == "__main__":
    wishme()
    switch=True
    while switch:
        query=takecommand().lower()
        if 'wikipedia' in query:
            print("Searching Wikipedia")
            speak("Searching Wiksipedia.........")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            print("According to Wikipedia....")
            speak("According to Wikipedia....")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'play music' in query:
            music_dir="G:\\Vlog Music"
            songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
            speak("Playing Music for you Dear..")
            i=random.choice(songs)
            os.startfile(os.path.join(music_dir,i))
        elif 'play video' in query:
            video_dir="G:\\Vlog Videos"
            videos = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
            speak("Playing Videos for you Dear..")
            i=random.choice(videos)
            os.startfile(os.path.join(video_dir,i))
        elif 'open gallery' in query:
            gallery_dir="G:\\Holi Photos"
            photos= [f for f in os.listdir(gallery_dir) if f.endswith('.jpg') or f.endswith('.png')]
            speak("Opening Gallery for you Dear..")
            i=random.choice(photos)
            os.startfile(os.path.join(gallery_dir,i))
        elif 'time' in query:
            str_time=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir the time is {str_time}")
            speak(f"Sir the time is {str_time}")
        elif 'open code' in query:
            code_path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'open whatsapp' in query:
            whatsapp_path="C:\\Users\\DELL\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsapp_path)
        elif 'clear screen' in query:
            os.system("cls")
        elif 'email to israr' in query:
            try:
                print("What should i say?")
                speak("What should i say ?")
                content=takecommand()
                to="reciever@gmail.com"
                send_email(to,content)
                print("Email Has Been Sent !! ")
                speak("Email Has Been Sent !! ")
            except Exception as e:
                print(e)
                speak("Sorry !! My Friend Sarwar Bhai I am not able to send email right now")
        elif 'quit' in query:
            speak("Have A Nice Day Sir !! Good Bye")
            switch=False
            exit(0)
