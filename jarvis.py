import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()    
engine = pyttsx3.init()

def speak (text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")
   elif "open whatsapp" in c.lower():
      webbrowser.open("https://whatsapp.com")
   elif "play perfect" in c.lower():
      webbrowser.open("https://youtu.be/cNGjD0VG4R8?si=GahrW3BaScsWXNhi")
   elif "play i wanna be yours" in c.lower():
      webbrowser.open("https://youtu.be/fukGbiPuBjU?si=X93J0qE6iHMMwZEK") 
   elif "play doremon " in c.lower():
      webbrowser.open("https://youtu.be/FJ_huAMvbNY?si=puPt7TIZ7-icIxPf")     

    

    


if __name__ == "__main__":
    speak("Initializing Jarvis")

while True:
    #Listen for the wake word jarvis
    # obtain audio from the microphone
        
    r = sr.Recognizer()

    print("Recognizing...")

    try:

        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source,timeout=2, phrase_time_limit=1)
        word = r.recognize_google(audio)
        if (word.lower() == "jarvis"):
            speak("Ya")
            #Listen for the command
            with sr.Microphone() as source:
             print("Jarvis active...")
             audio = r.listen(source,timeout=2, phrase_time_limit=1)
             command = r.recognize_google(audio)

             processcommand(command)

    except Exception as e:
     print("Error;{0}".format(e))      

             

     
