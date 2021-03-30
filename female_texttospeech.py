from gtts import gTTS  
import os 
txt =input("Enter the text:")
language = 'en'
speech = gTTS(text=txt, lang=language, slow=False)   
speech.save("text2speech.mp3")
os.system("start text2speech.mp3")
