#this program recognizes speech from audio files.
#start off with "(sudo) pip install SpeechRecognition"
#the audio file recorded has to be of the extention ".wav"
#save the audio file in the same folder where the program is stored and run the program


import speech_recognition as sr
audio_file=("test1.wav")    #test1.wav is the name of the audio file

r=sr.Recognizer()          #initialize recognizer

with sr.AudioFile(audio_file) as source:
    audio=r.record(source)         #reads audio file
try:
    print("audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("sorry, audio cant be understood")
except sr.RequestError:
    print("no results from google speech recognition")


