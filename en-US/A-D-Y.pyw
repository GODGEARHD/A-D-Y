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
from os import popen, remove, system
from pynput.keyboard import Key, Controller
from sys import exit
from random import randint
from time import sleep
from datetime import datetime
import wmi

r = sr.Recognizer()
keyboard = Controller()
numError = 0
activation = False
keywords = ["speak", "ADI", "hey"]
running = False

sao = wmi.WMI()
for process in sao.Win32_Process():
    if "SAO Utils.exe" == process.Name:
        running = True
        break


def start(phase, active):
    answers = [
        "Hi, I'm ADY, how can I help you?",
        "ADY ready to help!"]
    answer = None
    if phase == 0:
        answer = answers[randint(0, 1)]
    elif phase == 1:
        keystroke("")
        sleep(2.33)
        answer = "Yes?"
    myAudio = gTTS(text=answer, lang='en-US', slow=False)
    myAudio.save("audio.mp3")
    print(answer)
    playsound("audio.mp3")
    remove("audio.mp3")
    main(active)


def main(activated):

    with sr.Microphone() as origin:
        print("Say something...")
        playsound("start-listen.wav")
        try:
            sleep(0.3)
            audio = r.listen(origin, timeout=5, phrase_time_limit=5)
            playback(audio, activated)
        except Exception:
            playsound("stop-listen.wav")
            keystroke("")
            pass


def playback(audio, activationing):
    myText = ""
    try:
        myText = r.recognize_google(audio, language='en-US')
    except Exception:
        pass
    myText = myText + " "
    print(myText)
    playsound("stop-listen.wav")

    match myText:

        case "what's up dog ":
            answer = "Yo! Wassup?"
            tts(answer, "", False, "")

        case myText if myText == "f*** you b**** " or myText == "shut your b**** ass up " \
                       or myText == "fuck you bitch " or myText == "shut your bitch ass up ":
            answer = "Ah nigga don't hate me cuz I'm beautiful nigga. Maybe if you got rid of that old geegee ass " \
                     "haircut you'd got some bitches on your dick. Oh, better yet, maybe Tanisha'll call your dog " \
                     "ass if she ever stop fucking with that brain surgeon or lawyer she fucking with. Niggaaa"
            tts(answer, "", False, "")

        case "shut yourself down ":
            answer = "All right, if you need something from me, just tap the green button on the top left corner " \
                     "in SAO Utils. See you!"
            tts(answer, "bye", False, "")

        case myText if myText == "shut up " or myText == "cállate " or myText == "nothing ":
            answer = "All right, if you need something just let me know."
            tts(answer, "", False, "")

        case myText if myText == "put the music " or myText == "hit play " or myText == "put music ":
            answer = "Okay, playing multimedia"
            tts(answer, "play", False, "")

        case myText if myText == "stop the music " or myText == "hit pause ":
            answer = "Gucci, pausing multimedia"
            tts(answer, "play", False, "")

        case myText if myText == "go to the next song " or myText == "pasa a otra canción " or myText == "next song ":
            answer = "Okay, going to the next song in the list"
            tts(answer, "next", False, "")

        case myText if myText == "go to the previous song " or myText == "put the last song " \
                       or myText == "previous song ":
            answer = "Okay, going back to the previous song"
            tts(answer, "previous", False, "")

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
            tts(answer, "presentation", False, "")

        case myText if myText == "power off the PC " or myText == "power off the computer " \
                       or myText == "power off the system " or myText == "power off the session":
            answer = "Okay, powering off the PC. See you when you turn it on again!"
            tts(answer, "", False, "")

        case myText if myText == "restart the PC " or myText == "restart the computer " \
                       or myText == "restart the system " or myText == "restart the session":
            answer = "Right I'm gonna restart your PC. Wait till I do it, it'll be just a moment."
            tts(answer, "reboot", False, "")

        case myText if myText == "lock the PC " or myText == "lock the computer " \
                       or myText == "lock the system " or myText == "lock the session":
            answer = "Locking the PC's session..."
            tts(answer, "lock", False, "")

        case myText if myText == "put the PC to sleep " or myText == "put the computer to sleep " \
                       or myText == "put the system to sleep " or myText == "put the session to sleep":
            answer = "Okay, putting the system in sleep mode."
            tts(answer, "suspend", False, "")

        case myText if "search in google " in myText or "search in Google " in myText:
            answer = "Vale, espera que lo busco y te lo enseño"
            tts(answer, "search", False, myText[17:-1])

        case myText if myText == "tell me the time " or myText == "what time is it ":
            date = datetime.now()
            answer = "Right now, it's " + date.time().strftime("%H:%M")
            tts(answer, "", False, "")

        case myText if myText == "tell me the date " or myText == "what day is it today ":
            locale.getlocale()
            date = datetime.now()
            answer = "Today is " + date.date().strftime("%A, %d of %B, %Y")
            tts(answer, "", False, "")

        case myText if myText == "switch to Spanish " or myText == "change to Spanish ":
            respuesta = "Okay, switching main program's language to: Spanish"
            tts(respuesta, "language", False, "")

        case myText if "open " in myText:
            answer = "Okay, opening " + myText[5:-1]
            tts(answer, myText[5:-1], True, "")

        case _:
            if activationing and myText != " ":
                answer = "what the fuck? what did you say?"
                tts(answer, "error", False, myText)


def tts(audio, name, isprogram, text):
    try:
        if name == "presentation":
            print(audio)
            playsound("presentation.mp3")
        else:
            myAudio = gTTS(text=audio, lang='en-US', slow=False)
            myAudio.save("audio.mp3")
            print(audio)
            playsound("audio.mp3")
            remove("audio.mp3")

        if isprogram:
            app(name)
            keystroke("")

        match name:

            case "error":
                myError = gTTS(text=text, lang='es-ES', slow=False)
                myError.save("audio.mp3")
                playsound("audio.mp3")
                remove("audio.mp3")
                keystroke("")

            case "bye":
                keystroke("")
                exit()

            case "play":
                keystroke("play")
                keystroke("")

            case "previous":
                keystroke("previous")
                keystroke("")

            case "next":
                keystroke("next")
                keystroke("")

            case "shutdown":
                keystroke("")
                system("shutdown.exe -s -t 0")

            case "reboot":
                keystroke("")
                system("shutdown.exe -r -t 0")

            case "lock":
                keystroke("")
                system("rundll32.exe user32.dll,LockWorkStation")

            case "suspend":
                keystroke("")
                system("powercfg -h off")
                system("rundll32.exe powrProf.dll, SetSuspendState Sleep")

            case "language":
                exit()
                """f = open("../config.ini", "w+")
                f.write("language = 'es-ES' ")
                f.close()
                exit()"""

            case "search":
                system("python -m webbrowser -t \"https://google.es/search?q=" + text.replace(" ", "+") + "\"")
                keystroke("")

            case _:
                keystroke("")

    except Exception:
        pass


def app(program):
    path = "\"..\\Links\\" + program + ".lnk\""
    popen(path)


# noinspection PyTypeChecker
def keystroke(media):
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


def background(origen):
    try:
        audio = r.listen(origen, timeout=7, phrase_time_limit=3)
        myText = r.recognize_google(audio, language='en-US', show_all=False)
        myText = myText.split(' ')
        print(myText)
        for i in keywords:
            if i in myText:
                start(1, True)
                break
            else:
                pass
    except Exception:
        print("Waiting to listen to the keyword...")


if __name__ == "__main__":
    activation = True
    start(0, activation)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            background(source)
