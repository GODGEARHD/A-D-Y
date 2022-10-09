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

r = sr.Recognizer()
keyboard = Controller()
numError = 0
activation = False
keywords = ["habla", "háblame", "ADI"]


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
    main(active)


def main(activated):

    with sr.Microphone() as source:
        print("Di algo...")
        playsound("start-listen.wav")
        try:
            sleep(0.3)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            playback(audio, activated)
        except Exception:
            playsound("stop-listen.wav")
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
    playsound("stop-listen.wav")

    if myText == "hola buenas ":
        respuesta = "alo prresidentess"
        tts(respuesta, "", False, "")

    elif myText == "me cago en tu madre " or myText == "mecagoentuputamadre ":
        respuesta = "Y yo en la tuya que se me abre hijueperra"
        tts(respuesta, "", False, "")

    elif myText == "apágate ":
        respuesta = "Vale, si necesitas algo de mí, toca el botón verde que tienes arriba a la izquierda en sao " \
                    "utils. ¡Nos vemos!"
        tts(respuesta, "bye", False, "")

    elif myText == "calla " or myText == "cállate " or myText == "nada ":
        respuesta = "Vale, si necesitas algo avísame"
        tts(respuesta, "", False, "")

    elif myText == "pon la música " or myText == "dale al play " or myText == "pon música ":
        respuesta = "Vale, reproduciendo multimedia"
        tts(respuesta, "play", False, "")

    elif myText == "para la música " or myText == "dale al pause ":
        respuesta = "Gucci, pausando multimedia"
        tts(respuesta, "play", False, "")

    elif myText == "pasa otra canción " or myText == "pasa a otra canción " or myText == "siguiente canción ":
        respuesta = "Vale, pasando a la siguiente canción en la lista de reproducción"
        tts(respuesta, "next", False, "")

    elif myText == "vuelve una canción hacia atrás " or myText == "pon la última canción " \
            or myText == "canción anterior ":
        respuesta = "Okay, vuelvo a la canción anterior"
        tts(respuesta, "previous", False, "")

    elif myText == "preséntate " or myText == "quién eres ":
        respuesta = "Vale, allá voy. Hola, me llamo ADY, acortado de \"Advanced Development auxiliarY\". Soy una " \
                    "asistente de voz creada por Carlos Maristegui, o End, como prefieras llamarle. Aún estoy en " \
                    "desarrollo, pero creo que ya soy capaz de hacer cositas interesantes. Por ejemplo, puedo abrir " \
                    "el programa que quieras, puedo reproducir o pausar tu música, también puedo ir a la canción " \
                    "anterior, ir a la siguiente, y también puedo imitar a IlloJuan... ¿No me crees? Espera, que te " \
                    "hago una demostración. Aló prresidentess. ¿A que se me da bien? Además, Si me insultas , " \
                    "que espero que no lo hagas por el bien de tu ordenador, puedo responderte con otro insulto. " \
                    "¿Quieres saber más? Bueno, si me dices algo que no entiendo, te diré en voz alta lo que he " \
                    "entendido, para que así puedas darle una vuelta, porque a lo mejor la culpa es tuya por no " \
                    "vocalizar. Por último, puedo encender, reiniciar, suspender, o bloquear tu ordenador, y así " \
                    "no tienes que gastar energías en darle al botoncito. En resumen, soy ADY, y soy tu nueva " \
                    "asistente personal. ¡Encantada de conocerte!"
        tts(respuesta, "presentation", False, "")

    elif myText == "apaga el PC " or myText == "apaga el ordenador " or myText == "apaga el equipo " \
            or myText == "apaga el sistema " or myText == "apaga la sesión":
        respuesta = "Vale, voy a apagar tu ordenador. ¡Nos vemos cuando lo vuelvas a encender!"
        tts(respuesta, "shutdown", False, "")

    elif myText == "reinicia el PC " or myText == "reinicia el ordenador " or myText == "reinicia el equipo " \
            or myText == "reinicia el sistema " or myText == "reinicia la sesión":
        respuesta = "De una, voy a reiniciar tu ordenador. Espera mientras lo hago, no tardo nada."
        tts(respuesta, "reboot", False, "")

    elif myText == "bloquea el PC " or myText == "bloquea el ordenador " or myText == "bloquea el equipo " \
            or myText == "bloquea el sistema " or myText == "bloquea la sesión":
        respuesta = "Bloqueando sesión del PC..."
        tts(respuesta, "lock", False, "")

    elif myText == "suspende el PC " or myText == "suspende el ordenador " or myText == "suspende el equipo " \
            or myText == "suspende el sistema " or myText == "suspende la sesión":
        respuesta = "Okay, poniendo el sistema en modo suspensión."
        tts(respuesta, "suspend", False, "")

    elif "busca en google " in myText or "busca en Google " in myText:
        respuesta = "Vale, espera que lo busco y te lo enseño"
        tts(respuesta, "search", False, myText[16:-1])

    elif myText == "dime la hora " or myText == "qué hora es ":
        date = datetime.now()
        respuesta = "La hora actual es " + date.time().strftime("%H:%M")
        tts(respuesta, "", False, "")

    elif myText == "dime la fecha " or myText == "qué día es hoy ":
        locale.getlocale()
        date = datetime.now()
        respuesta = "Hoy es " + date.date().strftime("%A, %d de %B de %Y")
        tts(respuesta, "", False, "")

    elif myText == "cambia inglés " or myText == "cambia a inglés ":
        respuesta = "Vale, cambiando el idioma del programa principal a: Inglés"
        tts(respuesta, "language", False, "")

    elif "abre " in myText:
        respuesta = "okay, abriendo " + myText[5:-1]
        tts(respuesta, myText[5:-1], True, "")

    else:
        if activationing and myText != " ":
            respuesta = "guatafak? qué has dicho?"
            tts(respuesta, "error", False, myText)


def tts(audio, name, isprogram, text):
    try:
        if name == "presentation":
            print(audio)
            playsound("presentation.mp3")
        else:
            myAudio = gTTS(text=audio, lang='es-ES', slow=False)
            myAudio.save("audio.mp3")
            print(audio)
            playsound("audio.mp3")
            remove("audio.mp3")

        if isprogram:
            app(name)
            keystroke("")

        elif name == "error":
            myError = gTTS(text=text, lang='es-ES', slow=False)
            myError.save("audio.mp3")
            playsound("audio.mp3")
            remove("audio.mp3")
            keystroke("")

        elif name == "bye":
            keystroke("")
            exit()

        elif name == "play":
            keystroke("play")
            keystroke("")

        elif name == "previous":
            keystroke("previous")
            keystroke("")

        elif name == "next":
            keystroke("next")
            keystroke("")

        elif name == "shutdown":
            keystroke("")
            system("shutdown.exe -s -t 0")

        elif name == "reboot":
            keystroke("")
            system("shutdown.exe -r -t 0")

        elif name == "lock":
            keystroke("")
            system("rundll32.exe user32.dll,LockWorkStation")

        elif name == "suspend":
            keystroke("")
            system("powercfg -h off")
            system("rundll32.exe powrProf.dll, SetSuspendState Sleep")

        elif name == "language":
            system("python \".\\en-US\\A-D-Y.pyw\"")
            start(0, activation)

        elif name == "search":
            system("python -m webbrowser -t \"https://google.es/search?q=" + text.replace(" ", "+") + "\"")
            keystroke("")

        else:
            keystroke("")

    except Exception:
        pass


def app(program):
    path = "\"..\\Links\\" + program + ".lnk\""
    popen(path)


# noinspection PyTypeChecker
def keystroke(media):
    if media == "play":
        keyboard.press(Key.media_play_pause)

    elif media == "previous":
        keyboard.press(Key.media_previous)

    elif media == "next":
        keyboard.press(Key.media_next)

    else:
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


if __name__ == "__main__":
    activation = True
    start(0, activation)
    r = sr.Recognizer()
    with sr.Microphone() as fuente:
        while True:
            background(fuente)
