import pyautogui as py
import time
import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Say something:")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except sr.WaitTimeoutError:
            print("Speech Recognition timed out. No speech detected.")

def type_text(text):
    py.typewrite(text, interval=0.01)
    py.press("Enter")

print("Starting in 5 seconds...")
time.sleep(5)

while True:
    spoken_text = listen()
    if spoken_text:
        type_text(spoken_text)
        time.sleep(1)
