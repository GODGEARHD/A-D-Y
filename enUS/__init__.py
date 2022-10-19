"""
IMPORTANT!!!!

This program is suposed to be used along with SAO Utils, in which you have to assign Ctrl+Alt+Shift+U as
the shortcut to open/close its interface.

But even if you don't want to use SAO Utils, this code should work absolutely fine, but be careful if you have
assigned the shortcut mentioned before, as ADY will use that shortcut.
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
keywords = ["speak", "ADI", "Adi", "hey", "80"]


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
            playsound(".\\enUS\\start-listen.wav")
        else:
            playsound("./enUS/start-listen.wav")
        try:
            audio = r.listen(origin, timeout=5, phrase_time_limit=3)
            return playback(audio, active, run)
        except Exception:
            if ostype == "nt":
                playsound(".\\enUS\\stop-listen.wav")
            else:
                playsound("./enUS/stop-listen.wav")
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
        playsound(".\\enUS\\stop-listen.wav")
    else:
        playsound("./enUS/stop-listen.wav")

    match myText:

        case "what's up dog ":
            answer = "Yo! Wassup?"
            tts(answer, "", False, "", run)

        case myText if myText == "f*** you b**** " or myText == "shut your b**** ass up " \
                       or myText == "fuck you bitch " or myText == "shut your bitch ass up ":
            answer = "Ah nigga don't hate me cuz I'm beautiful nigga. Maybe if you got rid of that old geegee ass " \
                     "haircut you'd got some bitches on your dick. Oh, better yet, maybe Tanisha'll call your dog " \
                     "ass if she ever stop fucking with that brain surgeon or lawyer she fucking with. Niggaaa"
            tts(answer, "", False, "", run)

        case "shut yourself down ":
            answer = "All right, if you need something from me, just tap the green button on the top left corner " \
                     "in SAO Utils. See you!"
            tts(answer, "bye", False, "", run)

        case myText if myText == "shut up " or myText == "cállate " or myText == "nothing ":
            answer = "All right, if you need something just let me know."
            tts(answer, "", False, "", run)

        case myText if myText == "put the music " or myText == "hit play " or myText == "put music ":
            answer = "Okay, playing multimedia"
            tts(answer, "play", False, "", run)

        case myText if myText == "stop the music " or myText == "hit pause ":
            answer = "Gucci, pausing multimedia"
            tts(answer, "play", False, "", run)

        case myText if myText == "go to the next song " or myText == "pasa a otra canción " or myText == "next song ":
            answer = "Okay, going to the next song in the list"
            tts(answer, "next", False, "", run)

        case myText if myText == "go to the previous song " or myText == "put the last song " \
                       or myText == "previous song ":
            answer = "Okay, going back to the previous song"
            tts(answer, "previous", False, "", run)

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
            tts(answer, "presentation", False, "", run)

        case myText if myText == "power off the PC " or myText == "power off the computer " \
                       or myText == "power off the system " or myText == "power off the session":
            answer = "Okay, powering off the PC. See you when you turn it on again!"
            tts(answer, "", False, "", run)

        case myText if myText == "restart the PC " or myText == "restart the computer " \
                       or myText == "restart the system " or myText == "restart the session":
            answer = "Right I'm gonna restart your PC. Wait till I do it, it'll be just a moment."
            tts(answer, "reboot", False, "", run)

        case myText if myText == "lock the PC " or myText == "lock the computer " \
                       or myText == "lock the system " or myText == "lock the session":
            answer = "Locking the PC's session..."
            tts(answer, "lock", False, "", run)

        case myText if myText == "put the PC to sleep " or myText == "put the computer to sleep " \
                       or myText == "put the system to sleep " or myText == "put the session to sleep":
            answer = "Okay, putting the system in sleep mode."
            tts(answer, "suspend", False, "", run)

        case myText if "search in google " in myText or "search in Google " in myText:
            answer = "Vale, espera que lo busco y te lo enseño"
            tts(answer, "search", False, myText[17:-1], run)

        case myText if myText == "tell me the time " or myText == "what time is it ":
            date = datetime.now()
            answer = "Right now, it's " + date.time().strftime("%H:%M")
            tts(answer, "", False, "", run)

        case myText if myText == "tell me the date " or myText == "what day is it today ":
            locale.getlocale()
            date = datetime.now()
            answer = "Today is " + date.date().strftime("%A, %d of %B, %Y")
            tts(answer, "", False, "", run)

        case myText if myText == "switch to Spanish " or myText == "change to Spanish " or myText == "cambia español " \
                       or myText == "cambia a español ":
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
        path = "\"..\\Links\\" + program + ".lnk\""
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
        myText = myText.split(' ')
        if "80" in myText:
            print(['ADY'])
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
        image = Image.open(".\\LOGO-ADY.png")
    else:
        image = Image.open("./LOGO-ADY.png")
    menu = (item('Cambiar a: Español', lambda: change(icon), visible=True),
            item('Turn On/Off caps notifier', lambda: caps_config("notifier"), visible=True),
            item('Turn On/Off dictated caps', lambda: caps_config("audio"), visible=True),
            item('Exit', lambda: close(icon), visible=True))
    icon = pystray.Icon("Ady", image, "A-D-Y running...", menu)
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
        """if returned == "spanish":
            return returned
        elif exiting:
            exiting = False
            return "exit"
        else:"""
        sr.Recognizer()
        with sr.Microphone() as fuente:
            while True:
                if llamada:
                    continue
                else:
                    returned2 = background(fuente, sao)
                    if returned2 == "spanish":
                        return returned2
                    elif exiting:
                        exiting = False
                        return "exit"
                    else:
                        continue
