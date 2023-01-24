"""
IMPORTANTE!!!!

Este programa está pensado para ser usado junto con SAO Utils, donde tendrás que tener asignado Ctrl+Alt+Shift+U
como atajo de teclado para abrir/cerrar su interfaz.

Aunque, si no quieres utilizar SAO Utils, este programa debería funcionar perfectamente y sin problemas. Pero
ten cuidado, ya que si tienes asignado el atajo anteriormente mencionado, ADY lo usará y hará lo que sea que haga ese
atajo.

-------------------------------------------------------------------------------------------------------------------

AÚN MÁS IMPORTANTE!!!!

A partir de la versión 0.5.9, he modificado parte del código (además de haber añadido nuevo código (mucho)),
por lo que A-D-Y tiene su propia interfaz, y ahora *NO* utiliza SAO Utils para absolutamente nada.

NOTA: La interfaz está todavía bastante verde, así que no esperes que sea demasiado sofisticada ;)
"""

import threading, keyboard, pystray, json, speech_recognition as sr
from esES.modules import tts, playback
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
    from win32con import VK_CAPITAL, VK_SCROLL, VK_NUMLOCK

returned2 = None
sao = False
exiting = False
icon = None
if ostype == "nt":
    mayus = GetKeyState(VK_CAPITAL)
    scroll = GetKeyState(VK_SCROLL)
    num = GetKeyState(VK_NUMLOCK)
notification_sent = False
mayus_notifier = None
mayus_audio = None

r = sr.Recognizer()
keywords = ["háblame", "ADI", "oye ADI"]


def locks_check():
    global mayus
    global scroll
    global num
    while True:
        sleep(0.01)
        mayus = GetKeyState(VK_CAPITAL)
        scroll = GetKeyState(VK_SCROLL)
        num = GetKeyState(VK_NUMLOCK)
        if mayus == 0:
            mayus = False
        elif mayus == 1:
            mayus = True
        if scroll == 0:
            scroll = False
        elif scroll == 1:
            scroll = True
        if num == 0:
            num = False
        elif num == 1:
            num = True


def caps_config(param):
    global mayus_notifier
    global mayus_audio
    if param == "notifier":
        if mayus_notifier:
            mayus_notifier = False
            f = open("config.ini", "w")
            f.write(f"language = 'es-ES'\n"
                    f"mayus_notifier = {str(mayus_notifier)}\n"
                    f"mayus_audio = {str(mayus_audio)}\n--EOF--")
            f.close()
        elif not mayus_notifier:
            mayus_notifier = True
            f = open("config.ini", "w")
            f.write(f"language = 'es-ES'\n"
                    f"mayus_notifier = {str(mayus_notifier)}\n"
                    f"mayus_audio = {str(mayus_audio)}\n--EOF--")
            f.close()
    elif param == "audio":
        if mayus_audio:
            mayus_audio = False
            f = open("config.ini", "w")
            f.write(f"language = 'es-ES'\n"
                    f"mayus_notifier = {str(mayus_notifier)}\n"
                    f"mayus_audio = {str(mayus_audio)}\n--EOF--")
            f.close()
        elif not mayus_audio:
            mayus_audio = True
            f = open("config.ini", "w")
            f.write(f"language = 'es-ES'\n"
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
            print("mayúsculas desactivadas")
            if notification_sent:
                icono.remove_notification()
            icono.notify("Mayús Desactivadas", "A-D-Y")
            notification_sent = True
        elif not mayus:
            mayus = True
            print("mayúsculas activadas")
            if notification_sent:
                icono.remove_notification()
            icono.notify("Mayús Activadas", "A-D-Y")
            notification_sent = True
    if mayus_audio:
        if mayus:
            if not mayus_notifier:
                mayus = False
                print("mayúsculas desactivadas")
            playsound(".\\esES\\caps.mp3")
        elif not mayus:
            if not mayus_notifier:
                mayus = True
                print("mayúsculas activadas")
            playsound(".\\esES\\noCaps.mp3")


def start(phase, active, run):
    respuestas = [
        "Hola, soy ADY, ¿en qué te puedo ayudar?",
        "¡ADY lista para ayudar!"]
    respuesta = None
    if phase == 0:
        keystroke("show", run)
        if ostype == "nt":
            playsound(".\\audio\\windowShow.wav")
        else:
            playsound("./audio/windowShow.wav")
        # sleep(2.33)
        respuesta = respuestas[randint(0, 1)]
    elif phase == 1:
        if run:
            keystroke("show", run)
            # sleep(2.33)
            if ostype == "nt":
                playsound(".\\audio\\windowShow.wav")
            else:
                playsound("./audio/windowShow.wav")
            # sleep(2.33)
        respuesta = "¿Sí?"
    myAudio = gTTS(text=respuesta, lang='es-ES', slow=False)
    myAudio.save("audio.mp3")
    print(respuesta)
    playsound("audio.mp3")
    remove("audio.mp3")
    return main(active, run)


def main(active, run):
    global mayus_notifier
    global mayus_audio
    global exiting
    global icon
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source=source, duration=0.5)
        print("Di algo...")
        if ostype == "nt":
            playsound(".\\audio\\startListen.wav")
        else:
            playsound("./audio/startListen.wav")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=3)
            return playback.main(mayus_notifier, mayus_audio, exiting, icon, audio, active, run)
        except Exception:
            if ostype == "nt":
                playsound(".\\audio\\stopListen.wav")
                sleep(0.2)
                playsound(".\\audio\\windowHide.wav")
            else:
                playsound("./audio/stopListen.wav")
                sleep(0.2)
                playsound("./audio/windowHide.wav")
            if run:
                keystroke("hide", run)
            pass


def background(origen, run):
    global exiting
    try:
        audio = r.listen(origen, timeout=7, phrase_time_limit=3)
        myText = r.recognize_google(audio, language='es-ES', show_all=False)
        match myText:
            case myText if "Adri" in myText:
                myText = str(myText).replace("Adri", "ADI")
                print(myText)
            case myText if "Javi" in myText:
                myText = str(myText).replace("Javi", "ADI")
                print(myText)
            case myText if "a ti" in myText:
                myText = str(myText).replace("a ti", "ADI")
                print(myText)
            case myText if "osiadie" in myText:
                myText = str(myText).replace("osiadie", "ADI")
                print(myText)
            case myText if "oyaji" in myText:
                myText = str(myText).replace("oyaji", "ADI")
                print(myText)
            case _:
                print(myText)
        for i in keywords:
            if i in myText:
                return start(1, True, run)
                # keystroke("shortcut", run)
            else:
                pass
    except Exception:
        print("Esperando a escuchar la palabra clave...")


def change(icono=icon):
    global returned2
    global exiting
    global sao
    returned2 = "english"
    exiting = True
    f = open("config.ini", "w")
    f.write(f"language = 'en-US'\n"
            f"mayus_notifier = {str(mayus_notifier)}\n"
            f"mayus_audio = {str(mayus_audio)}\n--EOF--")
    f.close()
    keystroke("hide", sao)
    icono.stop()


def close(icono=icon):
    icono.stop()


def tray():
    global returned2
    global icon
    global mayus
    global scroll
    global num
    keyboard.add_hotkey('capslock', lambda: caps_notifications(icon))
    if ostype == "nt":
        # keyboard.add_hotkey('capslock', lambda: osd.caps_lock(mayus))
        # keyboard.add_hotkey('scrlk', lambda: osd.scroll_lock(scroll))
        # keyboard.add_hotkey('numlock', lambda: osd.num_lock(num))
        image = Image.open(".\\image\\LOGO-ADY.png")
    else:
        image = Image.open("./image/LOGO-ADY.png")
    menu = (item('Change to: English', lambda: change(icon), visible=True),
            item('Activar/Desactivar notificador de Mayus', lambda: caps_config("notifier"), visible=True),
            item('Activar/Desactivar dictado de Mayus', lambda: caps_config("audio"), visible=True),
            item('Salir', lambda: close(icon), visible=True))
    icon = pystray.Icon("Ady", image, "A-D-Y", menu)
    icon.run()
    """if ostype == "nt":
        osd.end()"""
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
    t3 = threading.Thread(target=locks_check)
    t3.daemon = True
    t3.start()
    while True:
        if t1.is_alive() and t2.is_alive():
            sleep(0.01)
            continue
        else:
            global mayus
            global scroll
            global num
            mayus = GetKeyState(VK_CAPITAL)
            scroll = GetKeyState(VK_SCROLL)
            num = GetKeyState(VK_NUMLOCK)
            # keyboard.unhook_all_hotkeys()
            return returned2


def __init__():
    global sao
    global returned2
    global exiting
    # keyboard.add_hotkey('ctrl + alt + shift + a', lambda: start(1, True, sao))
    returned2 = start(0, True, sao)
    if returned2 == "english":
        return "english"
    elif exiting:
        exiting = False
        return "exit"
    else:
        sr.Recognizer()
        with sr.Microphone() as fuente:
            r.adjust_for_ambient_noise(source=fuente, duration=0.5)
            while True:
                returned2 = background(fuente, sao)
                if returned2 == "english":
                    return returned2
                elif exiting:
                    exiting = False
                    return "exit"
                else:
                    continue
