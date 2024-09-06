import pyttsx3

# Initialize pyttsx3 with the Windows SAPI5 driver
engine = pyttsx3.init(driverName='sapi5')

engine.say("Hello, welcome to RoboSpeaker!")
engine.runAndWait()
