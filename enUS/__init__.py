"""
IMPORTANT!!!!

This program is suposed to be used along with SAO Utils, in which you have to assign Ctrl+Alt+Shift+U as
the shortcut to open/close its interface.

But even if you don't want to use SAO Utils, this code should work absolutely fine, but be careful if you have
assigned the shortcut mentioned before, as ADY will use that shortcut.

-------------------------------------------------------------------------------------------------------------------

EVEN MORE IMPORTANT!!!!

Right now, with the lastest release, I modified part of the code (as well as added new code (a lot of it)), so A-D-Y
has her own interface, and now she does *NOT* use SAO Utils at all.

NOTE: The interface is still in a very early stage, so don't expect it to be too fancy ;)
"""

import locale
import threading
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from os import popen, remove, system, name as ostype
from pynput.keyboard import Key, Controller
from sys import exit
from random import randint
from time import sleep
from datetime import datetime
import keyboard
from pystray import MenuItem as item
import pystray
from PIL import Image
from win32api import GetKeyState
from win32con import VK_CAPITAL
import json

returned2 = None
sao = False
exiting = False
icon = None
llamada = False
mayus = GetKeyState(VK_CAPITAL)
notification_sent = False
mayus_notifier = None
mayus_audio = None

r = sr.Recognizer()
Keyboard = Controller()
keywords = ["speak", "ADI", "Adi", "hey", "ADY"]


def caps_check():
    global mayus
    while True:
        sleep(0.01)
        mayus = GetKeyState(VK_CAPITAL)
        if mayus == 0:
            mayus = False
        elif mayus == 1:
            mayus = True


def caps_config(param):
    global mayus_notifier
    global mayus_audio
    if param == "notifier":
        if mayus_notifier:
            mayus_notifier = False
            f = open("config.ini", "w")
            f.write(f"language = 'en-US'\n"
                    f"mayus_notifier = {str(mayus_notifier)}\n"
                    f"mayus_audio = {str(mayus_audio)}\n--EOF--")
            f.close()
        elif not mayus_notifier:
            mayus_notifier = True
            f = open("config.ini", "w")
            f.write(f"language = 'en-US'\n"
                    f"mayus_notifier = {str(mayus_notifier)}\n"
                    f"mayus_audio = {str(mayus_audio)}\n--EOF--")
            f.close()
    elif param == "audio":
        if mayus_audio:
            mayus_audio = False
            f = open("config.ini", "w")
            f.write(f"language = 'en-US'\n"
                    f"mayus_notifier = {str(mayus_notifier)}\n"
                    f"mayus_audio = {str(mayus_audio)}\n--EOF--")
            f.close()
        elif not mayus_audio:
            mayus_audio = True
            f = open("config.ini", "w")
            f.write(f"language = 'en-US'\n"
                    f"mayus_notifier = {str(mayus_notifier)}\n"
                    f"mayus_audio = {str(mayus_audio)}\n--EOF--")
            f.close()


def caps_notifications(icono=icon):
    global mayus
    global mayus_notifier
    global mayus_audio
    global icon
    global notification_sent
    if mayus_notifier:
        if mayus:
            mayus = False
            print("caps off")
            if notification_sent:
                icono.remove_notification()
            icono.notify("Caps OFF", "A-D-Y")
            notification_sent = True
        elif not mayus:
            mayus = True
            print("caps on")
            if notification_sent:
                icono.remove_notification()
            icono.notify("Caps ON", "A-D-Y")
            notification_sent = True
    if mayus_audio:
        if mayus:
            if not mayus_notifier:
                mayus = False
                print("caps off")
            playsound(".\\enUS\\caps.mp3")
        elif not mayus:
            if not mayus_notifier:
                mayus = True
                print("caps on")
            playsound(".\\enUS\\noCaps.mp3")


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


def main(active, run):
    with sr.Microphone() as origin:
        print("Say something...")
        if ostype == "nt":
            playsound(".\\audio\\startListen.wav")
        else:
            playsound("./audio/startListen.wav")
        try:
            audio = r.listen(origin, timeout=5)
            return playback(audio, active, run)
        except Exception:
            if ostype == "nt":
                playsound(".\\audio\\stopListen.wav")
            else:
                playsound("./audio/stopListen.wav")
            if run:
                keystroke("", run)
            pass


def playback(audio, active, run):
    myText = ""
    try:
        myText = r.recognize_google(audio, language='en-US')
    except Exception:
        if run:
            keystroke("", run)
        pass
    myText = myText + " "
    print(myText)
    if ostype == "nt":
        playsound(".\\audio\\stopListen.wav")
    else:
        playsound("./audio/stopListen.wav")

    match myText:

        case myText if "what's up dog " in myText:
            answer = "Yo! Wassup?"
            tts(answer, "", False, "", run)

        case myText if "f*** you b**** " in myText or "shut your b**** ass up " in myText \
                       or "fuck you bitch " or "shut your bitch ass up ":
            answer = "Ah nigga don't hate me cuz I'm beautiful nigga. Maybe if you got rid of that old geegee ass " \
                     "haircut you'd got some bitches on your dick. Oh, better yet, maybe Tanisha'll call your dog " \
                     "ass if she ever stop fucking with that brain surgeon or lawyer she fucking with. Niggaaa"
            tts(answer, "", False, "", run)

        case myText if "shut yourself down " in myText:
            answer = "All right, if you need something from me, just tap the green button on the top left corner " \
                     "in SAO Utils. See you!"
            tts(answer, "bye", False, "", run)

        case myText if "shut up " in myText or "cállate " in myText or "nothing " in myText:
            answer = "All right, if you need something just let me know."
            tts(answer, "", False, "", run)

        case myText if "put the music " in myText or "hit play " in myText or "put music " in myText:
            answer = "Okay, playing multimedia"
            tts(answer, "play", False, "", run)

        case myText if "stop the music " in myText or "hit pause " in myText:
            answer = "Gucci, pausing multimedia"
            tts(answer, "play", False, "", run)

        case myText if "go to the next song " in myText or "pasa a otra canción " in myText or "next song " in myText:
            answer = "Okay, going to the next song in the list"
            tts(answer, "next", False, "", run)

        case myText if "go to the previous song " in myText or "put the last song " in myText \
                       or "previous song " in myText:
            answer = "Okay, going back to the previous song"
            tts(answer, "previous", False, "", run)

        case myText if "present yourself " in myText or "who are you " in myText:
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
            tts(answer, "presentation", False, "", run)

        case myText if "power off the PC " in myText or "power off the computer " in myText \
                       or "power off the system " in myText or "power off the session" in myText:
            answer = "Okay, powering off the PC. See you when you turn it on again!"
            tts(answer, "", False, "", run)

        case myText if "restart the PC " in myText or "restart the computer " in myText \
                       or "restart the system " in myText or "restart the session" in myText:
            answer = "Right I'm gonna restart your PC. Wait till I do it, it'll be just a moment."
            tts(answer, "reboot", False, "", run)

        case myText if "lock the PC " in myText or "lock the computer " in myText \
                       or "lock the system " in myText or "lock the session" in myText:
            answer = "Locking the PC's session..."
            tts(answer, "lock", False, "", run)

        case myText if "put the PC to sleep " in myText or "put the computer to sleep " in myText \
                       or "put the system to sleep " in myText or "put the session to sleep" in myText:
            answer = "Okay, putting the system in sleep mode."
            tts(answer, "suspend", False, "", run)

        case myText if "search in google " in myText or "search in Google " in myText:
            answer = "Vale, espera que lo busco y te lo enseño"
            tts(answer, "search", False, myText[17:-1], run)

        case myText if "tell me the time " in myText or "what time is it " in myText:
            date = datetime.now()
            answer = "Right now, it's " + date.time().strftime("%H:%M")
            tts(answer, "", False, "", run)

        case myText if "tell me the date " in myText or "what day is it today " in myText:
            locale.getlocale()
            date = datetime.now()
            answer = "Today is " + date.date().strftime("%A, %d of %B, %Y")
            tts(answer, "", False, "", run)

        case myText if "switch to Spanish " in myText or "change to Spanish " in myText or "cambia español " in myText \
                       or "cambia a español " in myText:
            # answer = "Okay, switching main program's language to: Spanish"
            answer = "I'm sorry, but I have this voice command function disabled because of a minor bug. If you want " \
                     "to change language, please use the tray icon."
            return tts(answer, "language", False, "", run)

        case myText if "open " in myText:
            answer = "Okay, opening " + myText[5:-1]
            tts(answer, myText[5:-1], True, "", run)

        case _:
            if active and myText != " ":
                answer = "what the fuck? what did you say?"
                tts(answer, "error", False, myText, run)


def tts(audio, name, isprogram, text, run):
    global mayus_notifier
    global mayus_audio
    global exiting
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
                if run:
                    keystroke("", run)

            case "bye":
                if run:
                    keystroke("", run)
                exit()

            case "play":
                keystroke("play", False)
                if run:
                    keystroke("", run)

            case "previous":
                keystroke("previous", False)
                if run:
                    keystroke("", run)

            case "next":
                keystroke("next", False)
                if run:
                    keystroke("", run)

            case "shutdown":
                if run:
                    keystroke("", run)
                if ostype == "nt":
                    system("shutdown.exe -s -t 0")
                else:
                    system("poweroff")

            case "reboot":
                if run:
                    keystroke("", run)
                if ostype == "nt":
                    system("shutdown.exe -r -t 0")
                else:
                    system("reboot")

            case "lock":
                if run:
                    keystroke("", run)
                if ostype == "nt":
                    system("rundll32.exe user32.dll,LockWorkStation")
                else:
                    pass

            case "suspend":
                if run:
                    keystroke("", run)
                if ostype == "nt":
                    system("powercfg -h off")
                    system("rundll32.exe powrProf.dll, SetSuspendState Sleep")
                else:
                    system("systemctl suspend")

            case "language":
                if run:
                    keystroke("", run)

            case "language2":
                f = open("config.ini", "w+")
                f.write(f"language = 'es-ES'\n"
                        f"mayus_notifier = {str(mayus_notifier)}\n"
                        f"mayus_audio = {str(mayus_audio)}\n--EOF--")
                f.close()
                exiting = True
                global icon
                # noinspection PyTypeChecker
                close(icon)
                return "spanish"

            case "search":
                system("python -m webbrowser -t \"https://google.es/search?q=" + text.replace(" ", "+") + "\"")
                if run:
                    keystroke("", run)

            case _:
                if run:
                    keystroke("", run)

    except Exception:
        pass


def app(program):
    if ostype == "nt":
        path = "\".\\programs\\" + program + ".lnk\""
        popen(path)
    else:
        pass


# noinspection PyTypeChecker
def keystroke(media, run):
    match media:

        case "play":
            Keyboard.press(Key.media_play_pause)

        case "previous":
            Keyboard.press(Key.media_previous)

        case "next":
            Keyboard.press(Key.media_next)

        case _:
            if run:
                Keyboard.press(Key.ctrl)
                Keyboard.press(Key.alt)
                Keyboard.press(Key.shift)
                Keyboard.press("u")
                Keyboard.release(Key.ctrl)
                Keyboard.release(Key.alt)
                Keyboard.release(Key.shift)
                Keyboard.release("u")


def background(origen, run):
    global exiting
    try:
        audio = r.listen(origen, timeout=7, phrase_time_limit=3)
        myText = r.recognize_google(audio, language='en-US', show_all=False)
        if "80" in myText:
            print(['ADY'])
            myText = "ADY"
        else:
            print(myText)
        for i in keywords:
            if i in myText:
                return start(1, True, run)
            else:
                pass
    except Exception:
        print("Waiting to listen to the keyword...")


def change(icono=icon):
    global returned2
    global exiting
    returned2 = "spanish"
    exiting = True
    f = open("config.ini", "w+")
    f.write(f"language = 'es-ES'\n"
            f"mayus_notifier = {str(mayus_notifier)}\n"
            f"mayus_audio = {str(mayus_audio)}\n--EOF--")
    f.close()
    keystroke("", sao)
    icono.stop()


def close(icono=icon):
    icono.stop()


def tray():
    global returned2
    global icon
    keyboard.add_hotkey('capslock', lambda: caps_notifications(icon))
    if ostype == "nt":
        image = Image.open(".\\image\\LOGO-ADY.png")
    else:
        image = Image.open("./image/LOGO-ADY.png")
    menu = (item('Cambiar a: Español', lambda: change(icon), visible=True),
            item('Turn On/Off caps notifier', lambda: caps_config("notifier"), visible=True),
            item('Turn On/Off dictated caps', lambda: caps_config("audio"), visible=True),
            item('Exit', lambda: close(icon), visible=True))
    icon = pystray.Icon("Ady", image, "A-D-Y", menu)
    icon.run()
    exit()


def initial(run):
    global returned2
    global sao
    global mayus_notifier
    global mayus_audio
    if ostype == "nt":
        config = ".\\config.ini"
    else:
        config = "./config.ini"
    with open(config, "r") as file:
        line = file.readlines()
        line1 = line[1]
        line2 = line[2]
        mayus_notifier = json.loads(line1[17:-1].lower())
        mayus_audio = json.loads(line2[14:-1].lower())
    sao = run
    t1 = threading.Thread(target=tray)
    t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=__init__)
    t2.daemon = True
    t2.start()
    t3 = threading.Thread(target=caps_check)
    t3.daemon = True
    t3.start()
    while True:
        if t1.is_alive() and t2.is_alive():
            sleep(0.01)
            continue
        else:
            global mayus
            mayus = GetKeyState(VK_CAPITAL)
            keyboard.unhook_all_hotkeys()
            return returned2


def __init__():
    global sao
    global returned2
    global exiting
    returned2 = start(0, True, sao)
    if returned2 == "spanish":
        return "spanish"
    elif exiting:
        exiting = False
        return "exit"
    else:
        sr.Recognizer()
        with sr.Microphone() as fuente:
            while True:
                returned2 = background(fuente, sao)
                if returned2 == "spanish":
                    return returned2
                elif exiting:
                    exiting = False
                    return "exit"
                else:
                    continue
