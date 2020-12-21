import speech_recognition as sr
import pyttsx3
from constants import *
from datetime import datetime
import reverse_geocoder as rg
import json

# Initialize the recognizer
r = sr.Recognizer()

# initialize the engine
engine = pyttsx3.init()

def prepare_voice_output(text):
    print(text)
    # initialize the engine
    engine.say(text)
    engine.runAndWait()


def prepare_input_from_voice():
    try:
        with sr.Microphone() as source:
            print("Listening ....")
            r.pause_threshold = 1
            voice_input = r.listen(source)
            # Using goggle to recognise audio
            text_input = r.recognize_google(voice_input)
            prepare_voice_output(text_input)
            return text_input.lower()
    except sr.UnknownValueError:
        prepare_voice_output(VALUEERROR)
        return None

def time():
    Time = datetime.now().strftime("%I:%M:%S")
    prepare_voice_output("the current time is")
    prepare_voice_output(Time)


def reverseGeocode(coordinates):
    result = rg.search(coordinates)
    r = json.loads(json.dumps(result))
    res_dict = r[0]
    res = []
    for key in res_dict.keys():
        res.append(res_dict[key])
    address = ' '.join([str(elem) for elem in res])
    # print("The address is: " + str(address))
    return address
