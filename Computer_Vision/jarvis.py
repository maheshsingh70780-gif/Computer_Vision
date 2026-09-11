import pyttsx3
import datetime
import webbrowser

# Initialize voice engine
engine = pyttsx3.init()

# Voice function
def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()


# Start Jarvis
speak("Hello Mahesh, I am Jarvis. How can I help you?")

while True:

    command = input("You: ").lower()

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello Mahesh! How are you?")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    # Date
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    # YouTube
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Google
    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # GitHub
    elif "github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # Instagram
    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    # Exit
    elif "exit" in command or "bye" in command or "stop" in command:
        speak("Goodbye Mahesh. Have a nice day!")
        break

    # Unknown command
    else:
        speak("Sorry, I don't understand this command.")