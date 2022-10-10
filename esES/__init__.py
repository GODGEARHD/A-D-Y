"""
IMPORTANTE!!!!

Este programa está pensado para ser usado junto con SAO Utils, donde tendrás que tener asignado Ctrl+Alt+Shift+U
como atajo de teclado para abrir/cerrar su interfaz.

Aunque, si no quieres utilizar SAO Utils, este programa debería funcionar perfectamente y sin problemas. Pero
ten cuidado, ya que si tienes asignado el atajo anteriormente mencionado, ADY lo usará y hará lo que sea que haga ese
atajo.
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
keywords = ["habla", "háblame", "ADI"]
running = False

sao = wmi.WMI()
for process in sao.Win32_Process():
    if "SAO Utils.exe" == process.Name:
        running = True
        break


def start(phase, active):
    respuestas = [
        "Hola, soy ADY, ¿en qué te puedo ayudar?",
        "¡ADY lista para ayudar!"]
    respuesta = None
    if phase == 0:
        respuesta = respuestas[randint(0, 1)]
    elif phase == 1:
        keystroke("")
        sleep(2.33)
        respuesta = "¿Sí?"
    myAudio = gTTS(text=respuesta, lang='es-ES', slow=False)
    myAudio.save("audio.mp3")
    print(respuesta)
    playsound("audio.mp3")
    remove("audio.mp3")
    return main(active)


def main(activated):

    with sr.Microphone() as source:
        print("Di algo...")
        playsound(".\\esES\\start-listen.wav")
        try:
            sleep(0.3)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            return playback(audio, activated)
        except Exception:
            playsound(".\\esES\\stop-listen.wav")
            keystroke("")
            pass


def playback(audio, activationing):
    myText = ""
    try:
        myText = r.recognize_google(audio, language='es-ES')
    except Exception:
        pass
    myText = myText + " "
    print(myText)
    playsound(".\\esES\\stop-listen.wav")

    match myText:

        case "hola buenas ":
            respuesta = "alo prresidentess"
            tts(respuesta, "", False, "")

        case myText if myText == "me cago en tu madre " or myText == "mecagoentuputamadre ":
            respuesta = "Y yo en la tuya que se me abre hijueperra"
            tts(respuesta, "", False, "")

        case "apágate ":
            respuesta = "Vale, si necesitas algo de mí, toca el botón verde que tienes arriba a la izquierda en sao " \
                "utils. ¡Nos vemos!"
            tts(respuesta, "bye", False, "")

        case myText if myText == "calla " or myText == "cállate " or myText == "nada ":
            respuesta = "Vale, si necesitas algo avísame"
            tts(respuesta, "", False, "")

        case myText if myText == "pon la música " or myText == "dale al play " or myText == "pon música ":
            respuesta = "Vale, reproduciendo multimedia"
            tts(respuesta, "play", False, "")

        case myText if myText == "para la música " or myText == "dale al pause ":
            respuesta = "Gucci, pausando multimedia"
            tts(respuesta, "play", False, "")

        case myText if myText == "pasa otra canción " or myText == "pasa a otra canción " \
                       or myText == "siguiente canción ":
            respuesta = "Vale, pasando a la siguiente canción en la lista de reproducción"
            tts(respuesta, "next", False, "")

        case myText if myText == "vuelve una canción hacia atrás " or myText == "pon la última canción " \
                       or myText == "canción anterior ":
            respuesta = "Okay, vuelvo a la canción anterior"
            tts(respuesta, "previous", False, "")

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
            tts(respuesta, "presentation", False, "")

        case myText if myText == "apaga el PC " or myText == "apaga el ordenador " or myText == "apaga el equipo " \
                       or myText == "apaga el sistema " or myText == "apaga la sesión":
            respuesta = "Vale, voy a apagar tu ordenador. ¡Nos vemos cuando lo vuelvas a encender!"
            tts(respuesta, "shutdown", False, "")

        case myText if myText == "reinicia el PC " or myText == "reinicia el ordenador " \
                       or myText == "reinicia el equipo " or myText == "reinicia el sistema " \
                       or myText == "reinicia la sesión":
            respuesta = "De una, voy a reiniciar tu ordenador. Espera mientras lo hago, no tardo nada."
            tts(respuesta, "reboot", False, "")

        case myText if myText == "bloquea el PC " or myText == "bloquea el ordenador " \
                       or myText == "bloquea el equipo " or myText == "bloquea el sistema " \
                       or myText == "bloquea la sesión":
            respuesta = "Bloqueando sesión del PC..."
            tts(respuesta, "lock", False, "")

        case myText if myText == "suspende el PC " or myText == "suspende el ordenador " \
                       or myText == "suspende el equipo " or myText == "suspende el sistema " \
                       or myText == "suspende la sesión":
            respuesta = "Okay, poniendo el sistema en modo suspensión."
            tts(respuesta, "suspend", False, "")

        case myText if "busca en google " in myText or "busca en Google " in myText:
            respuesta = "Vale, espera que lo busco y te lo enseño"
            tts(respuesta, "search", False, myText[16:-1])

        case myText if myText == "dime la hora " or myText == "qué hora es ":
            date = datetime.now()
            respuesta = "La hora actual es " + date.time().strftime("%H:%M")
            tts(respuesta, "", False, "")

        case myText if myText == "dime la fecha " or myText == "qué día es hoy ":
            locale.getlocale()
            date = datetime.now()
            respuesta = "Hoy es " + date.date().strftime("%A, %d de %B de %Y")
            tts(respuesta, "", False, "")

        case myText if myText == "cambia inglés " or myText == "cambia a inglés ":
            respuesta = "Vale, cambiando el idioma del programa principal a: Inglés"
            return tts(respuesta, "language", False, "")

        case myText if "abre " in myText:
            respuesta = "okay, abriendo " + myText[5:-1]
            tts(respuesta, myText[5:-1], True, "")

        case _:
            if activationing and myText != " ":
                respuesta = "guatafak? qué has dicho?"
                tts(respuesta, "error", False, myText)


def tts(audio, name, isprogram, text):
    try:
        if name == "presentation":
            print(audio)
            playsound(".\\esES\\presentation.mp3")
        else:
            myAudio = gTTS(text=audio, lang='es-ES', slow=False)
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
                f = open("config.ini", "w")
                f.write("language = 'en-US' ")
                f.close()
                return "english"

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
        myText = r.recognize_google(audio, language='es-ES', show_all=False)
        myText = myText.split(' ')
        print(myText)
        for i in keywords:
            if i in myText:
                start(1, True)
                break
            else:
                pass
    except Exception:
        print("Esperando a escuchar la palabra clave...")


def __init__():
    toggle = True
    returned = start(0, toggle)
    if returned == "english":
        return returned
    else:
        sr.Recognizer()
        with sr.Microphone() as fuente:
            while True:
                background(fuente)


if __name__ == "__main__":
    __init__()