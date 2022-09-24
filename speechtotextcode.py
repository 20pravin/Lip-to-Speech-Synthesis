import speech_recognition as sr
import time
r=sr.Recognizer()
r.dynamic_energy_threshold = 3000
with sr.Microphone() as source:
 print('Speak in: ')
 time.sleep(1)
 print('3')
 time.sleep(1)
 print('2')
 time.sleep(1)
 print('1')
 time.sleep(1)
 print('GO')
 audio=r.listen(source)
try:
 text=r.recognize_google(audio)
 print('Recognized text:-----> {}'.format(text))
except:
 print('Speak Properly')
 #we got Accuracy Level=75%