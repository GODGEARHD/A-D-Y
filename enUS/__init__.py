"""
IMPORTANT!!!!

This program is suposed to be used along with SAO Utils, in which you have to assign Ctrl+Alt+Shift+U as
the shortcut to open/close its interface.

But even if you don't want to use SAO Utils, this code should work absolutely fine, but be careful if you have
assigned the shortcut mentioned before, as ADY will use that shortcut.
"""

import locale
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from os import popen, remove, system, name as ostype
from pynput.keyboard import Key, Controller
from sys import exit
from random import randint
from time import sleep
from datetime import datetime

r = sr.Recognizer()
keyboard = Controller()
numError = 0
activation = False
keywords = ["speak", "ADI", "hey"]


def start(phase, active, run):
    answers = [
        "Hi, I'm ADY, how can I help you?",
        "ADY ready to help!"]
    answer = None
    if phase == 0:
        answer = answers[randint(0, 1)]
    elif phase == 1:
        if run:
            keystroke("", run)
            sleep(2.33)
        answer = "Yes?"
    myAudio = gTTS(text=answer, lang='en-US', slow=False)
    myAudio.save("audio.mp3")
    print(answer)
    playsound("audio.mp3")
    remove("audio.mp3")
    return main(active, run)


def main(activated, execution):
    with sr.Microphone() as origin:
        print("Say something...")
        if ostype == "nt":
            playsound(".\\enUS\\start-listen.wav")
        else:
            playsound("./enUS/start-listen.wav")
        try:
            sleep(0.1)
            audio = r.listen(origin, timeout=5, phrase_time_limit=5)
            return playback(audio, activated, execution)
        except Exception:
            if ostype == "nt":
                playsound(".\\enUS\\stop-listen.wav")
            else:
                playsound("./enUS/stop-listen.wav")
            if execution:
                keystroke("", execution)
            pass


def playback(audio, activationing, executioning):
    myText = ""
    try:
        myText = r.recognize_google(audio, language='en-US')
    except Exception:
        pass
    myText = myText + " "
    print(myText)
    if ostype == "nt":
        playsound(".\\enUS\\stop-listen.wav")
    else:
        playsound("./enUS/stop-listen.wav")

    match myText:

        case "what's up dog ":
            answer = "Yo! Wassup?"
            tts(answer, "", False, "", executioning)

        case myText if myText == "f*** you b**** " or myText == "shut your b**** ass up " \
                       or myText == "fuck you bitch " or myText == "shut your bitch ass up ":
            answer = "Ah nigga don't hate me cuz I'm beautiful nigga. Maybe if you got rid of that old geegee ass " \
                     "haircut you'd got some bitches on your dick. Oh, better yet, maybe Tanisha'll call your dog " \
                     "ass if she ever stop fucking with that brain surgeon or lawyer she fucking with. Niggaaa"
            tts(answer, "", False, "", executioning)

        case "shut yourself down ":
            answer = "All right, if you need something from me, just tap the green button on the top left corner " \
                     "in SAO Utils. See you!"
            tts(answer, "bye", False, "", executioning)

        case myText if myText == "shut up " or myText == "cállate " or myText == "nothing ":
            answer = "All right, if you need something just let me know."
            tts(answer, "", False, "", executioning)

        case myText if myText == "put the music " or myText == "hit play " or myText == "put music ":
            answer = "Okay, playing multimedia"
            tts(answer, "play", False, "", executioning)

        case myText if myText == "stop the music " or myText == "hit pause ":
            answer = "Gucci, pausing multimedia"
            tts(answer, "play", False, "", executioning)

        case myText if myText == "go to the next song " or myText == "pasa a otra canción " or myText == "next song ":
            answer = "Okay, going to the next song in the list"
            tts(answer, "next", False, "", executioning)

        case myText if myText == "go to the previous song " or myText == "put the last song " \
                       or myText == "previous song ":
            answer = "Okay, going back to the previous song"
            tts(answer, "previous", False, "", executioning)

        case myText if myText == "present yourself " or myText == "who are you ":
            answer = "Ok, here I go. Hello, my name is ADY, short for \"Advanced Development auxiliarY\". I'm a " \
                 "voice assistant created by Carlos Maristegui, or End, as you prefer to call him. I'm still " \
                 "under development, but I think I'm already capable of doing interesting things. For example, " \
                 "I can open the program you want, I can play or pause your music, I can also go to the previous " \
                 "song, go to the next one, and I can also imitate Lamar from GTA 5... Don't you believe me? Wait, " \
                 "let me show you. Ah nigga don't hate me cuz I'm beautiful. Don't I do it well? Also, if you insult " \
                 "me, which I hope you don't for the good of your computer, I can respond with another insult. You " \
                 "want to know more? Well, if you tell me something I don't understand, I'll tell you out loud what " \
                 "I understood, so that you can think about it, because maybe it's your fault for not vocalizing. " \
                 "Lastly, I can power on, restart, send to sleep mode, or lock your computer, so you don't have to " \
                 "spend energy hitting the button. Anyways, I'm ADY, and I'm your new personal assistant. Nice to " \
                 "meet you!"
            tts(answer, "presentation", False, "", executioning)

        case myText if myText == "power off the PC " or myText == "power off the computer " \
                       or myText == "power off the system " or myText == "power off the session":
            answer = "Okay, powering off the PC. See you when you turn it on again!"
            tts(answer, "", False, "", executioning)

        case myText if myText == "restart the PC " or myText == "restart the computer " \
                       or myText == "restart the system " or myText == "restart the session":
            answer = "Right I'm gonna restart your PC. Wait till I do it, it'll be just a moment."
            tts(answer, "reboot", False, "", executioning)

        case myText if myText == "lock the PC " or myText == "lock the computer " \
                       or myText == "lock the system " or myText == "lock the session":
            answer = "Locking the PC's session..."
            tts(answer, "lock", False, "", executioning)

        case myText if myText == "put the PC to sleep " or myText == "put the computer to sleep " \
                       or myText == "put the system to sleep " or myText == "put the session to sleep":
            answer = "Okay, putting the system in sleep mode."
            tts(answer, "suspend", False, "", executioning)

        case myText if "search in google " in myText or "search in Google " in myText:
            answer = "Vale, espera que lo busco y te lo enseño"
            tts(answer, "search", False, myText[17:-1], executioning)

        case myText if myText == "tell me the time " or myText == "what time is it ":
            date = datetime.now()
            answer = "Right now, it's " + date.time().strftime("%H:%M")
            tts(answer, "", False, "", executioning)

        case myText if myText == "tell me the date " or myText == "what day is it today ":
            locale.getlocale()
            date = datetime.now()
            answer = "Today is " + date.date().strftime("%A, %d of %B, %Y")
            tts(answer, "", False, "", executioning)

        case myText if myText == "switch to Spanish " or myText == "change to Spanish " or myText == "cambia español " \
                       or myText == "cambia a español ":
            respuesta = "Okay, switching main program's language to: Spanish"
            return tts(respuesta, "language", False, "", executioning)

        case myText if "open " in myText:
            answer = "Okay, opening " + myText[5:-1]
            tts(answer, myText[5:-1], True, "", executioning)

        case _:
            if activationing and myText != " ":
                answer = "what the fuck? what did you say?"
                tts(answer, "error", False, myText, executioning)


def tts(audio, name, isprogram, text, running):
    try:
        if name == "presentation":
            print(audio)
            if ostype == "nt":
                sound = ".\\enUS\\presentation.mp3"
            else:
                sound = "./enUS/presentation.mp3"
            playsound(sound)
        else:
            myAudio = gTTS(text=audio, lang='en-US', slow=False)
            myAudio.save("audio.mp3")
            print(audio)
            playsound("audio.mp3")
            remove("audio.mp3")

        if isprogram:
            app(name)

        match name:

            case "error":
                myError = gTTS(text=text, lang='en-US', slow=False)
                myError.save("audio.mp3")
                playsound("audio.mp3")
                remove("audio.mp3")
                if running:
                    keystroke("", running)

            case "bye":
                if running:
                    keystroke("", running)
                exit()

            case "play":
                keystroke("play", False)
                if running:
                    keystroke("", running)

            case "previous":
                keystroke("previous", False)
                if running:
                    keystroke("", running)

            case "next":
                keystroke("next", False)
                if running:
                    keystroke("", running)

            case "shutdown":
                if running:
                    keystroke("", running)
                system("shutdown.exe -s -t 0")

            case "reboot":
                if running:
                    keystroke("", running)
                system("shutdown.exe -r -t 0")

            case "lock":
                if running:
                    keystroke("", running)
                system("rundll32.exe user32.dll,LockWorkStation")

            case "suspend":
                if running:
                    keystroke("", running)
                system("powercfg -h off")
                system("rundll32.exe powrProf.dll, SetSuspendState Sleep")

            case "language":
                f = open("config.ini", "w+")
                f.write("language = 'es-ES' ")
                f.close()
                return "spanish"

            case "search":
                system("python -m webbrowser -t \"https://google.es/search?q=" + text.replace(" ", "+") + "\"")
                if running:
                    keystroke("", running)

            case _:
                if running:
                    keystroke("", running)

    except Exception:
        pass


def app(program):
    if ostype == "nt":
        path = "\"..\\Links\\" + program + ".lnk\""
        popen(path)
    else:
        pass


# noinspection PyTypeChecker
def keystroke(media, running):
    match media:

        case "play":
            keyboard.press(Key.media_play_pause)

        case "previous":
            keyboard.press(Key.media_previous)

        case "next":
            keyboard.press(Key.media_next)

        case _:
            if running:
                keyboard.press(Key.ctrl)
                keyboard.press(Key.alt)
                keyboard.press(Key.shift)
                keyboard.press("u")
                keyboard.release(Key.ctrl)
                keyboard.release(Key.alt)
                keyboard.release(Key.shift)
                keyboard.release("u")


def background(origen, run):
    try:
        audio = r.listen(origen, timeout=7, phrase_time_limit=3)
        myText = r.recognize_google(audio, language='en-US', show_all=False)
        myText = myText.split(' ')
        print(myText)
        for i in keywords:
            if i in myText:
                start(1, True, run)
                break
            else:
                pass
    except Exception:
        print("Waiting to listen to the keyword...")


def __init__(run):
    returned = start(0, True, run)
    if returned == "spanish":
        return returned
    else:
        sr.Recognizer()
        with sr.Microphone() as fuente:
            while True:
                background(fuente, run)
