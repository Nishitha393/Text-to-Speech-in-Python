import PyPDF2
import pyttsx3
path = open('power.pdf', 'rb')
pr = PyPDF2.PdfFileReader(path)
fp = pr.getPage(1)
text = fp.extractText()
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
