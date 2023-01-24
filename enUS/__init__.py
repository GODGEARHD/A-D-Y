"""
IMPORTANT!!!!

This program is suposed to be used along with SAO Utils, in which you have to assign Ctrl+Alt+Shift+U as
the shortcut to open/close its interface.

But even if you don't want to use SAO Utils, this code should work absolutely fine, but be careful if you have
assigned the shortcut mentioned before, as ADY will use that shortcut.

-------------------------------------------------------------------------------------------------------------------

EVEN MORE IMPORTANT!!!!

From version 0.5.9 onwards, I've modified part of the code (as well as added new code (a lot of it)), so A-D-Y
has her own interface, and now she does *NOT* use SAO Utils at all.

NOTE: The interface is still in a very early stage, so don't expect it to be too fancy ;)
"""

import threading, keyboard, pystray, json, speech_recognition as sr
from enUS.modules import tts, playback
from modules.keystroke import keystroke
from gtts import gTTS
from playsound import playsound
from os import remove, name as ostype
from sys import exit
from random import randint
from time import sleep
from pystray import MenuItem as item
from PIL import Image
if ostype == "nt":
    from win32api import GetKeyState
    from win32con import VK_CAPITAL

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
    global mayus_notifier
    global mayus_audio
    global exiting
    global icon
    with sr.Microphone() as origin:
        print("Say something...")
        if ostype == "nt":
            playsound(".\\audio\\startListen.wav")
        else:
            playsound("./audio/startListen.wav")
        try:
            audio = r.listen(origin, timeout=5)
            return playback.main(mayus_notifier, mayus_audio, exiting, icon, audio, active, run)
        except Exception:
            if ostype == "nt":
                playsound(".\\audio\\stopListen.wav")
            else:
                playsound("./audio/stopListen.wav")
            if run:
                keystroke("", run)
            pass


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
