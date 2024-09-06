import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Swaathy")
    engine = pyttsx3.init(driverName='sapi5')
    
    while True:
        x = input("Enter what you want me to speak (or 'q' to quit): ")
        if x.lower() == "q":
            print("Exiting RoboSpeaker. Goodbye!")
            break
        engine.say(x)
        engine.runAndWait()
