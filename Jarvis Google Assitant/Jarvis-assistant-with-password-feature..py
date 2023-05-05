from tkinter import *
import pyttsx3 
import speech_recognition as sr
from tkinter.ttk import *
from time import strftime 
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser as wb
wb.register('chrome', None)
import webbrowser
import os
import smtplib
import turtle
import time


window = Tk()
window.title("JARVIS ASSISTANT")
window.geometry("730x510")
window.config(bg="grey")
label = Label(text="***----Welcome To Jarvis----***",font=("bold","16"))
label.place(relx=0.3034, rely=0.123)

def import_File():
    # window.destroy()
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        r.energy_threshold=5000
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query

    def Password(password_inp):
            password = "thugs"
            passs = str(password)
            if (passs == str(password_inp)):
                    speak("Access Granted")
                    print("Access Granted")
                    return True
                    
            else:
                speak("Access Not Granted")
                print("Access Not Granted")
                return False
    
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('mehr68909@gmail.com', 'qwerty@7513')
        server.sendmail('mehr68909@gmail.com', to, content)
        server.close()

    def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("Good Morning!")
                print("Good Morning!")

            elif hour>=12 and hour<18:
                speak("Good Afternoon!")
                print("Good Afternoon!")   

            else:
                speak("Good Evening!") 
                print("Good Evening!") 

            speak("I am Jarvis Assistant Sir. Please tell me how may I help you?")
            print("I am Jarvis Assistant Sir. Please tell me how may I help you?")

    def my_idle():
        
        wishMe()
        while True:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                wb.open('https://www.youtube.com')
                True 
            elif 'open google' in query:
                wb.open('https://www.google.com')
            elif 'tell about today weather' in query:
                wb.open('https://weather.com/en-PK/weather/today/l/cf5522d2a67ba145bdaac907e186a9f94f0eb96047723746d0ffe6a138be77c2')    
                True
            elif 'open whatsapp' in query:
                wb.open('https://web.whatsapp.com/')
                True
            elif 'display the time' in query:
                clock = Tk() 
                clock.title('Clock') 

    
                def time(): 
                    string = strftime('%H:%M:%S %p') 
                    lbl.config(text = string) 
                    lbl.after(1000, time) 


                lbl = Label(clock, font = ('calibri', 40, 'bold'), 
                            background = 'purple', 
                            foreground = 'white') 

                lbl.pack(anchor = 'center') 
                time() 

                mainloop() 
            
            elif 'open analogue clock' in query:
                wndw = turtle.Screen()
                wndw.bgcolor("black")
                wndw.setup(width=600, height=600)
                wndw.title("Analogue Clock")
                wndw.tracer(0)

                # Create the drawing pen
                pen = turtle.Turtle()
                pen.hideturtle()
                pen.speed(0)
                pen.pensize(3)


                def draw_clock(hr, mn, sec, pen):

                    # Draw clock face
                    pen.up()
                    pen.goto(0, 210)
                    pen.setheading(180)
                    pen.color("green")
                    pen.pendown()
                    pen.circle(210)

                    # Draw hour hashes
                    pen.up()
                    pen.goto(0, 0)
                    pen.setheading(90)

                    for _ in range(12):
                        pen.fd(190)
                        pen.pendown()
                        pen.fd(20)
                        pen.penup()
                        pen.goto(0, 0)
                        pen.rt(30)

                    # Draw the hands
                    # Each tuple in list hands describes the color, the length
                    # and the divisor for the angle
                    hands = [("white", 80, 12), ("blue", 150, 60), ("red", 110, 60)]
                    time_set = (hr, mn, sec)

                    for hand in hands:
                        time_part = time_set[hands.index(hand)]
                        angle = (time_part/hand[2])*360
                        pen.penup()
                        pen.goto(0, 0)
                        pen.color(hand[0])
                        pen.setheading(90)
                        pen.rt(angle)
                        pen.pendown()
                        pen.fd(hand[1])


                while True:
                    hr = int(time.strftime("%I"))
                    mn = int(time.strftime("%M"))
                    sec = int(time.strftime("%S"))

                    draw_clock(hr, mn, sec, pen)
                    wndw.update()
                    time.sleep(1)
                    pen.clear()

                wndw.mainloop()
                
            elif 'open timer' in query:
                try:
                    import tkinter as tk
                except ImportError:
                    import Tkinter as tk   
                class Timer:
                    def __init__(self, parent):
                        # variable storing time
                        self.seconds = 0
                        # label displaying time
                        self.label = tk.Label(parent, text="0 s", font="Arial 30", width=10)
                        self.label.pack()
                        # start the timer
                        self.label.after(1000, self.refresh_label)

                    def refresh_label(self):
                        """ refresh the content of the label every second """
                        # increment the time
                        self.seconds += 1
                        # display the new time
                        self.label.configure(text="%i s" % self.seconds)
                        # request tkinter to call self.refresh after 1s (the delay is given in ms)
                        self.label.after(1000, self.refresh_label)

                if __name__ == "__main__":
                    root = tk.Tk()
                    timer = Timer(root)
                    root.mainloop()
                
                
                    
            elif 'search from google' in query:
                sr.Microphone(device_index=1)
                r = sr.Recognizer()
                r.energy_threshold=5000
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    print("Speak The word you want to search:----")
                    r.pause_threshold = 1
                
                try:
                
                    text = r.recognize_google(audio)
                    print(("You said:",format(text)))
                    url="https://www.google.com/search?q="
                    search_url=url+text
                    webbrowser.open(search_url)
                except:
                    print("Can't Recognize")
            
            elif 'open chrome' in query:
                codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)
            elif 'open stack overflow' in query:
                wb.open('https://stackoverflow.com')
                True 
            elif 'play music' in query:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))
            elif  'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime) 
                speak(f"Sir, The time is {strTime}")
            elif 'open code' in query:
                codePath = r"C:\Users\Mehr Kashif\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                os.startfile(codePath)
            elif 'open python' in query:
                codePath = r"C:\Users\Mehr Kashif\AppData\Local\Programs\Python\Python310\Lib\idlelib\idle.pyw"
                os.startfile(codePath)
            elif 'open powerpoint' in query:
                codePath = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
                os.startfile(codePath)
            elif 'open world' in query:
                codePath = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                os.startfile(codePath)
            elif 'open excel' in query:
                codePath = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
                os.startfile(codePath)
            elif 'quit' in query:
                exit()


            elif 'email to kashif' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "kashi.heart12@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Mehmood. I am not able to send this email") 
            elif 'search from youtube' in query:
                sr.Microphone(device_index=1)
                r = sr.Recognizer()
                r.energy_threshold=5000
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    print("Speak The word you want to search:----")
                    r.pause_threshold = 1
                
                try:
                
                    text = r.recognize_google(audio)
                    print(("You said:",format(text)))
                    url="https://www.youtube.com/results?search_query="
                    search_url=url+text
                    webbrowser.open(search_url)
                except:
                    print("Can't Recognize")
        
    window.destroy()    
    speak("Thisparticular file is password protected.") 
    print("This particular file is password protected.")
    speak("Kindly provide the password to Access.")
    print("Kindly provide the password to Access.")
    while True:
        
        pas = input("Enter The Password  : ")
        if Password(pas)==True:
            my_idle()
        else:
            passsss = takeCommand()
            print("User Said :",passsss)
            if Password(passsss)==True:
                my_idle()
        
def Exit():
    exit()

StartButton = Button(text="Start", command= import_File )
StartButton.place(relx=0.425, rely=0.295)

EndButton = Button(text="Exit", command=Exit )
EndButton.place(relx=0.425, rely=0.555)


mainloop()