import pyttsx3

textSpeech = pyttsx3.init()

text = input("Enter Text you want to convert into Speech : ")
textSpeech.say(text)
textSpeech.runAndWait()
