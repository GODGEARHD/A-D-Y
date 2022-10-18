"""
IMPORTANTE!!!!

Este programa está pensado para ser usado junto con SAO Utils, donde tendrás que tener asignado Ctrl+Alt+Shift+U
como atajo de teclado para abrir/cerrar su interfaz.

Aunque, si no quieres utilizar SAO Utils, este programa debería funcionar perfectamente y sin problemas. Pero
ten cuidado, ya que si tienes asignado el atajo anteriormente mencionado, ADY lo usará y hará lo que sea que haga ese
atajo.
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

returned = None
sao = False
exiting = False
icon = None
llamada = False
mayus = GetKeyState(VK_CAPITAL)
mayus_option = True

r = sr.Recognizer()
Keyboard = Controller()
keywords = ["habla", "háblame", "ADI", "hey"]


def capscheck():
    global mayus
    while True:
        sleep(0.01)
        mayus = GetKeyState(VK_CAPITAL)
        if mayus == 0:
            mayus = False
        elif mayus == 1:
            mayus = True


def caps_option():
    global mayus_option
    if mayus_option:
        mayus_option = False
    elif not mayus_option:
        mayus_option = True


def caps():
    global mayus
    global mayus_option
    if mayus_option:
        if mayus:
            mayus = False
            print("mayúsculas desactivadas")
            playsound(".\\esES\\noCaps.mp3")
        elif not mayus:
            mayus = True
            print("mayúsculas activadas")
            playsound(".\\esES\\caps.mp3")
    else:
        pass


def start(phase, active, run):
    respuestas = [
        "Hola, soy ADY, ¿en qué te puedo ayudar?",
        "¡ADY lista para ayudar!"]
    respuesta = None
    if phase == 0:
        respuesta = respuestas[randint(0, 1)]
    elif phase == 1:
        if run:
            keystroke("", run)
            sleep(2.33)
        respuesta = "¿Sí?"
    myAudio = gTTS(text=respuesta, lang='es-ES', slow=False)
    myAudio.save("audio.mp3")
    print(respuesta)
    playsound("audio.mp3")
    remove("audio.mp3")
    return main(active, run)


def main(active, run):
    with sr.Microphone() as source:
        print("Di algo...")
        if ostype == "nt":
            playsound(".\\esES\\start-listen.wav")
        else:
            playsound("./esES/start-listen.wav")
        try:
            # sleep(0.1)
            # audio = r.listen(source, timeout=5, phrase_time_limit=5)
            audio = r.listen(source, timeout=5, phrase_time_limit=3)
            return playback(audio, active, run)
        except Exception:
            if ostype == "nt":
                playsound(".\\esES\\stop-listen.wav")
            else:
                playsound("./esES/stop-listen.wav")
            if run:
                keystroke("", run)
            pass


def playback(audio, active, run):
    myText = ""
    try:
        myText = r.recognize_google(audio, language='es-ES')
    except Exception:
        if run:
            keystroke("", run)
        pass
    myText = myText + " "
    print(myText)
    if ostype == "nt":
        playsound(".\\esES\\stop-listen.wav")
    else:
        playsound("./esES/stop-listen.wav")

    match myText:

        case "hola buenas ":
            respuesta = "alo prresidentess"
            tts(respuesta, "", False, "", run)

        case myText if myText == "me cago en tu madre " or myText == "mecagoentuputamadre ":
            respuesta = "Y yo en la tuya que se me abre hijueperra"
            tts(respuesta, "", False, "", run)

        case "apágate ":
            respuesta = "Vale, si necesitas algo de mí, toca el botón verde que tienes arriba a la izquierda en sao " \
                        "utils. ¡Nos vemos!"
            tts(respuesta, "bye", False, "", run)

        case myText if "calla " in myText or "cállate " in myText or "nada " in myText:
            respuesta = "Vale, si necesitas algo avísame"
            tts(respuesta, "", False, "", run)

        case myText if myText == "pon la música " or myText == "dale al play " or myText == "pon música ":
            respuesta = "Vale, reproduciendo multimedia"
            tts(respuesta, "play", False, "", run)

        case myText if myText == "para la música " or myText == "dale al pause ":
            respuesta = "Gucci, pausando multimedia"
            tts(respuesta, "play", False, "", run)

        case myText if myText == "pasa otra canción " or myText == "pasa a otra canción " \
                       or myText == "siguiente canción ":
            respuesta = "Vale, pasando a la siguiente canción en la lista de reproducción"
            tts(respuesta, "next", False, "", run)

        case myText if myText == "vuelve una canción hacia atrás " or myText == "pon la última canción " \
                       or myText == "canción anterior ":
            respuesta = "Okay, vuelvo a la canción anterior"
            tts(respuesta, "previous", False, "", run)

        case myText if myText == "preséntate " or myText == "quién eres ":
            respuesta = "Vale, allá voy. Hola, me llamo ADY, acortado de \"Advanced Development auxiliarY\". Soy una " \
                    "asistente de voz creada por Carlos Maristegui, o End, como prefieras llamarle. Aún estoy en " \
                    "desarrollo, pero creo que ya soy capaz de hacer cositas interesantes. Por ejemplo, puedo abrir " \
                    "el programa que quieras, puedo reproducir o pausar tu música, también puedo ir a la canción " \
                    "anterior, ir a la siguiente, y también puedo imitar a IlloJuan... ¿No me crees? Espera, que te " \
                    "hago una demostración. Aló prresidentess. ¿A que se me da bien? Además, si me insultas, " \
                    "que espero que no lo hagas por el bien de tu ordenador, puedo responderte con otro insulto. " \
                    "¿Quieres saber más? Bueno, si me dices algo que no entiendo, te diré en voz alta lo que he " \
                    "entendido, para que así puedas darle una vuelta, porque a lo mejor la culpa es tuya por no " \
                    "vocalizar. Por último, puedo encender, reiniciar, suspender, o bloquear tu ordenador, y así " \
                    "no tienes que gastar energías en darle al botoncito. En resumen, soy ADY, y soy tu nueva " \
                    "asistente personal. ¡Encantada de conocerte!"
            tts(respuesta, "presentation", False, "", run)

        case myText if myText == "apaga el PC " or myText == "apaga el ordenador " or myText == "apaga el equipo " \
                       or myText == "apaga el sistema " or myText == "apaga la sesión":
            respuesta = "Vale, voy a apagar tu ordenador. ¡Nos vemos cuando lo vuelvas a encender!"
            tts(respuesta, "shutdown", False, "", run)

        case myText if myText == "reinicia el PC " or myText == "reinicia el ordenador " \
                       or myText == "reinicia el equipo " or myText == "reinicia el sistema " \
                       or myText == "reinicia la sesión":
            respuesta = "De una, voy a reiniciar tu ordenador. Espera mientras lo hago, no tardo nada."
            tts(respuesta, "reboot", False, "", run)

        case myText if myText == "bloquea el PC " or myText == "bloquea el ordenador " \
                       or myText == "bloquea el equipo " or myText == "bloquea el sistema " \
                       or myText == "bloquea la sesión":
            respuesta = "Bloqueando sesión del PC..."
            tts(respuesta, "lock", False, "", run)

        case myText if myText == "suspende el PC " or myText == "suspende el ordenador " \
                       or myText == "suspende el equipo " or myText == "suspende el sistema " \
                       or myText == "suspende la sesión":
            respuesta = "Okay, poniendo el sistema en modo suspensión."
            tts(respuesta, "suspend", False, "", run)

        case myText if "busca en google " in myText or "busca en Google " in myText:
            respuesta = "Vale, espera que lo busco y te lo enseño"
            tts(respuesta, "search", False, myText[16:-1], run)

        case myText if myText == "dime la hora " or myText == "qué hora es ":
            date = datetime.now()
            respuesta = "La hora actual es " + date.time().strftime("%H:%M")
            tts(respuesta, "", False, "", run)

        case myText if myText == "dime la fecha " or myText == "qué día es hoy ":
            locale.getlocale()
            date = datetime.now()
            months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
                      "Octubre", "Noviembre", "Diciembre"]
            weekdays = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
            weekday = weekdays[datetime.today().weekday()]
            day = date.day
            month = months[date.month - 1]
            year = date.year
            respuesta = f"Hoy es {weekday}, {day} de {month} del {year}"
            tts(respuesta, "", False, "", run)

        case myText if myText == "cambia inglés " or myText == "cambia a inglés " or myText == "change to English " \
                       or myText == "switch to English ":
            respuesta = "Vale, cambiando el idioma del programa principal a: Inglés"
            return tts(respuesta, "language", False, "", run)

        case myText if "abre " in myText or "ábreme " in myText:
            respuesta = "okay, abriendo " + myText[5:-1]
            tts(respuesta, myText[5:-1], True, "", run)

        case _:
            if active and myText != " ":
                respuesta = "guatafak? qué has dicho?"
                tts(respuesta, "error", False, myText, run)


def tts(audio, name, isprogram, text, run):
    try:
        if name == "presentation":
            print(audio)
            if ostype == "nt":
                sound = ".\\esES\\presentation.mp3"
            else:
                sound = "./esES/presentation.mp3"
            playsound(sound)
        else:
            myAudio = gTTS(text=audio, lang='es-ES', slow=False)
            myAudio.save("audio.mp3")
            print(audio)
            playsound("audio.mp3")
            remove("audio.mp3")

        if isprogram:
            app(name)

        match name:

            case "error":
                myError = gTTS(text=text, lang='es-ES', slow=False)
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
                f = open("config.ini", "w")
                f.write("language = 'en-US' ")
                f.close()
                # noinspection PyTypeChecker
                close(icon)
                return "english"

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

        case "shortcut":
            Keyboard.press(Key.ctrl)
            Keyboard.press(Key.alt)
            Keyboard.press(Key.shift)
            Keyboard.press("a")
            Keyboard.release(Key.ctrl)
            Keyboard.release(Key.alt)
            Keyboard.release(Key.shift)
            Keyboard.release("a")

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
    """global llamada
    if callback:
        llamada = True
        calling = start(1, True, run)
        llamada = False
        return calling
    else:"""
    try:
        audio = r.listen(origen, timeout=7, phrase_time_limit=3)
        myText = r.recognize_google(audio, language='es-ES', show_all=False)
        myText = myText.split(' ')
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
    global returned
    global exiting
    global sao
    returned = "english"
    exiting = True
    keystroke("", sao)
    icono.stop()


def close(icono=icon):
    icono.stop()


def tray():
    global returned
    global icon
    if ostype == "nt":
        image = Image.open(".\\LOGO-ADY.png")
    else:
        image = Image.open("./LOGO-ADY.png")
    menu = (item('Change to: English', lambda: change(icon), visible=True),
            item('Activar/Desactivar dictado de Mayus', lambda: caps_option(), visible=True),
            item('Salir', lambda: close(icon), visible=True))
    icon = pystray.Icon("name", image, "A-D-Y en ejecución...", menu)
    icon.run()
    exit()


def initial(run):
    global returned
    global sao
    sao = run
    keyboard.add_hotkey('capslock', lambda: caps())
    t1 = threading.Thread(target=tray)
    t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=__init__)
    t2.daemon = True
    t2.start()
    t3 = threading.Thread(target=capscheck)
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
            return returned


def __init__():
    global sao
    global returned
    global exiting
    # keyboard.add_hotkey('ctrl + alt + shift + a', lambda: start(1, True, sao))
    returned = start(0, True, sao)
    if returned == "english":
        return returned
    elif exiting:
        exiting = False
        return "exit"
    else:
        if returned == "english":
            return returned
        elif exiting:
            exiting = False
            return "exit"
        else:
            sr.Recognizer()
            with sr.Microphone() as fuente:
                while True:
                    if llamada:
                        continue
                    else:
                        returned = background(fuente, sao)
                        if returned == "english":
                            return returned
                        elif exiting:
                            exiting = False
                            return "exit"
                        else:
                            continue
