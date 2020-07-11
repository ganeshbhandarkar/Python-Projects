import pyttsx3

text = input("Enter to pronounce:\n")
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()