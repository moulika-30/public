import os, pyttsx3
import speech_recognition as sr
def take_commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognising")
            Query = r.recognize_google(audio)
            print("The Query is ",Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        import time
        time.sleep(2)
        return Query
def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
Speak("Do you want to shutdown the computer?")
while True:
    command = take_commands()

    if "exit" in command:
        Speak("ok sir, let me exit")
        break
    if "yes" in command:
        Speak("ok sir thank you computer will shutdown now")
        os.system("shutdown /s /t 30")
    if "no" in command:
        Speak("ok sir no problem")
        break
   
