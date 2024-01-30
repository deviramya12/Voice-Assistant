import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech using PyAudio
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError as e:
        print(f"Request to Google Speech Recognition service failed: {e}")
        return ""

# Function to get the current time
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."

# Function to get the current date
def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"Today's date is {current_date}."

# Function to search the web using Google
def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}.")

# Main function to execute the voice assistant
def main():
    speak("Hello! I am your basic voice assistant. How can I assist you today?")

    while True:
        query = recognize_speech()

        if "hello" in query:
            speak("Hello! How can I help you today?")

        elif "time" in query:
            current_time = get_time()
            speak(current_time)

        elif "date" in query:
            current_date = get_date()
            speak(current_date)

        elif "search" in query:
            speak("What would you like me to search for?")
            search_query = recognize_speech()
            search_web(search_query)

        elif "exit" in query or "bye" in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
