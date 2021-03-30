import pyttsx3 
c= pyttsx3.init() 
c.setProperty('rate', 100) 
c.setProperty('volume', 0.5) 
t=input()
c.say(t) 
c.runAndWait() 
