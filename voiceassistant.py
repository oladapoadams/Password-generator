import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed
engine.setProperty('voice', 'english')  # Select voice

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice
def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...🎤")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand, please repeat...")
        return ""
    except sr.RequestError:
        print("API unavailable")
        return ""

# Function to process commands
def respond_to_command(command):
    if "hello" in command:
        speak("Hey dapo How you doing?")
    
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "shutdown" in command:
        speak("Shutting down now. Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that.")

# Run the assistant
if __name__ == "__main__":
    speak("Voice assistant activated. How can I assist you?")
    while True:
        command = recognize_voice()
        if command:
            respond_to_command(command)
