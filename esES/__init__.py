"""
IMPORTANTE!!!!

Este programa está pensado para ser usado junto con SAO Utils, donde tendrás que tener asignado Ctrl+Alt+Shift+U
como atajo de teclado para abrir/cerrar su interfaz.

Aunque, si no quieres utilizar SAO Utils, este programa debería funcionar perfectamente y sin problemas. Pero
ten cuidado, ya que si tienes asignado el atajo anteriormente mencionado, ADY lo usará y hará lo que sea que haga ese
atajo.

-------------------------------------------------------------------------------------------------------------------

AÚN MÁ S IMPORTANTE!!!!

En este momento, con la última versión, he modificado parte del código (además de haber añadido nuevo código (mucho)),
por lo que A-D-Y tiene su propia interfaz, y ahora *NO* utiliza SAO Utils para absolutamente nada.

NOTA: La interfaz está todavía bastante verde, así que no esperes que sea demasiado sofisticada ;)
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
if ostype == "nt":
    from win32api import GetKeyState
    from win32con import VK_CAPITAL, VK_SCROLL, VK_NUMLOCK
import json
import osd
import AVMSpeechMath as sm

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
Keyboard = Controller()
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
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source=source, duration=0.5)
        print("Di algo...")
        if ostype == "nt":
            playsound(".\\audio\\startListen.wav")
        else:
            playsound("./audio/startListen.wav")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=3)
            return playback(audio, active, run)
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


def playback(audio, active, run):
    myText = ""
    try:
        myText = r.recognize_google(audio, language='es-ES')
    except Exception:
        if run:
            keystroke("hide", run)
        pass
    myText = myText + " "
    print(myText)
    if ostype == "nt":
        playsound(".\\audio\\stopListen.wav")
    else:
        playsound("./audio/stopListen.wav")

    match myText:

        case myText if "hola buenas " in myText:
            respuesta = "alo prresidentess"
            tts(respuesta, "", False, "", run)

        case myText if "me cago en tu madre " in myText or "mecagoentuputamadre " in myText:
            respuesta = "Y yo en la tuya que se me abre hijueperra"
            tts(respuesta, "", False, "", run)

        case myText if "apágate " in myText:
            # respuesta = "Vale, si necesitas algo de mí, toca el botón verde que tienes arriba a la izquierda en " \
            #            "sao utils. ¡Nos vemos!"
            respuesta = "Vale. Si me necesitas de nuevo, simplemente vuelve a ejecutarme. ¡Nos vemos!"
            tts(respuesta, "bye", False, "", run)

        case myText if "calla " in myText or "cállate " in myText or "nada " in myText:
            respuesta = "Vale, si necesitas algo avísame"
            tts(respuesta, "", False, "", run)

        case myText if "pon la música " in myText or "dale al play " in myText or "pon música " in myText:
            respuesta = "Vale, reproduciendo multimedia"
            tts(respuesta, "play", False, "", run)

        case myText if "para la música " in myText or "dale al pause " in myText:
            respuesta = "Gucci, pausando multimedia"
            tts(respuesta, "play", False, "", run)

        case myText if "pasa otra canción " in myText or "pasa a otra canción " in myText \
                       or "siguiente canción " in myText:
            respuesta = "Vale, pasando a la siguiente canción en la lista de reproducción"
            tts(respuesta, "next", False, "", run)

        case myText if "vuelve una canción hacia atrás " in myText or "pon la última canción " in myText \
                       or "canción anterior " in myText:
            respuesta = "Okay, vuelvo a la canción anterior"
            tts(respuesta, "previous", False, "", run)

        case myText if "preséntate " in myText or "quién eres " in myText:
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

        case myText if "apaga el PC " in myText or "apaga el ordenador " in myText or "apaga el equipo " in myText \
                       or "apaga el sistema " in myText or "apaga la sesión" in myText:
            respuesta = "Vale, voy a apagar tu ordenador. ¡Nos vemos cuando lo vuelvas a encender!"
            tts(respuesta, "shutdown", False, "", run)

        case myText if "reinicia el PC " in myText or "reinicia el ordenador " in myText \
                       or "reinicia el equipo " in myText or "reinicia el sistema " in myText \
                       or "reinicia la sesión" in myText:
            respuesta = "De una, voy a reiniciar tu ordenador. Espera mientras lo hago, no tardo nada."
            tts(respuesta, "reboot", False, "", run)

        case myText if "bloquea el PC " in myText or "bloquea el ordenador " in myText \
                       or "bloquea el equipo " in myText or "bloquea el sistema " in myText \
                       or "bloquea la sesión" in myText:
            respuesta = "Bloqueando sesión del PC..."
            tts(respuesta, "lock", False, "", run)

        case myText if "suspende el PC " in myText or "suspende el ordenador " in myText \
                       or "suspende el equipo " in myText or "suspende el sistema " in myText \
                       or "suspende la sesión" in myText:
            respuesta = "Okay, poniendo el sistema en modo suspensión."
            tts(respuesta, "suspend", False, "", run)

        case myText if "busca en google " in myText or "busca en Google " in myText:
            respuesta = "¿Qué quieres que busque exactamente?"
            tts(respuesta, "", False, "", False)
            with sr.Microphone() as source:
                # r.adjust_for_ambient_noise(source=source, duration=0.5)
                print("Di algo...")
                if ostype == "nt":
                    playsound(".\\audio\\startListen.wav")
                else:
                    playsound("./audio/startListen.wav")
                try:
                    audio = r.listen(source, timeout=5, phrase_time_limit=7)
                    myText = ""
                    try:
                        myText = r.recognize_google(audio, language='es-ES')
                    except Exception:
                        if run:
                            keystroke("hide", run)
                        pass
                    myText = myText + " "
                    print(myText)
                    if ostype == "nt":
                        playsound(".\\audio\\stopListen.wav")
                    else:
                        playsound("./audio/stopListen.wav")
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
            respuesta = "Vale, dame un segundo que lo busque"
            tts(respuesta, "search", False, myText, run)  # myText[16:-1]

        case myText if "dime la hora " in myText or "qué hora es " in myText:
            date = datetime.now()
            respuesta = "La hora actual es " + date.time().strftime("%H:%M")
            tts(respuesta, "", False, "", run)

        case myText if "dime la fecha " in myText or "qué día es hoy " in myText:
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

        case myText if "cambia inglés " in myText or "cambia a inglés " in myText or "change to English " in myText \
                       or "switch to English " in myText:
            # respuesta = "Vale, cambiando el idioma del programa principal a: Inglés"
            respuesta = "Lo siento, pero he dejado la función de cambio de idioma mediante comando de voz " \
                        "temporalmente desactivada por un pequeño bug que encontré hace un rato. Si quieres cambiar " \
                        "el idioma, por favor usa el icono que tienes en tu bandeja del sistema."
            return tts(respuesta, "language", False, "", run)

        case myText if "calcula " in myText or "calcula esto " in myText:
            respuesta = "¿Cuál es la operación?"
            tts(respuesta, "", False, "", False)
            with sr.Microphone() as source:
                # r.adjust_for_ambient_noise(source=source, duration=0.5)
                print("Di algo...")
                if ostype == "nt":
                    playsound(".\\audio\\startListen.wav")
                else:
                    playsound("./audio/startListen.wav")
                try:
                    audio = r.listen(source, timeout=5, phrase_time_limit=10)
                    myText = ""
                    try:
                        myText = r.recognize_google(audio, language='es-ES')
                    except Exception:
                        if run:
                            keystroke("hide", run)
                        pass
                    myText = myText + " "
                    print(myText)
                    if ostype == "nt":
                        playsound(".\\audio\\stopListen.wav")
                    else:
                        playsound("./audio/stopListen.wav")
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
            result = sm.getResult(myText)
            if result != "Unable to evaluate equation":
                tts(result, "calc", False, "", run)
            else:
                respuesta = "Oye, creo que te has equivocado al decirme la ecuación, no soy capaz de resolverla. " \
                            "Revísala y dímela otra vez."
                tts(respuesta, "calc", False, "", run)

        case myText if "abre " in myText or "ábreme " in myText:
            respuesta = "okay, abriendo " + myText[5:-1]
            tts(respuesta, myText[5:-1], True, "", run)

        case _:
            if active and myText != " ":
                respuesta = "guatafak? qué has dicho?"
                tts(respuesta, "error", False, myText, run)


def tts(audio, name, isprogram, text, run):
    global mayus_notifier
    global mayus_audio
    global exiting
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
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")

            case "bye":
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")
                """if ostype == "nt":
                    osd.end()"""
                exit()

            case "play":
                keystroke("play", False)
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")

            case "previous":
                keystroke("previous", False)
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")

            case "next":
                keystroke("next", False)
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")

            case "shutdown":
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")
                if ostype == "nt":
                    system("shutdown.exe -s -t 0")
                else:
                    system("poweroff")

            case "reboot":
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")
                if ostype == "nt":
                    system("shutdown.exe -r -t 0")
                else:
                    system("reboot")

            case "lock":
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")
                if ostype == "nt":
                    system("rundll32.exe user32.dll,LockWorkStation")
                else:
                    pass

            case "suspend":
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")
                if ostype == "nt":
                    system("powercfg -h off")
                    system("rundll32.exe powrProf.dll, SetSuspendState Sleep")
                else:
                    system("systemctl suspend")

            case "language":
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")

            case "language2":
                f = open("config.ini", "w")
                f.write(f"language = 'en-US'\n"
                        f"mayus_notifier = {str(mayus_notifier)}\n"
                        f"mayus_audio = {str(mayus_audio)}\n--EOF--")
                f.close()
                exiting = True
                global icon
                # noinspection PyTypeChecker
                close(icon)
                return "english"

            case "search":
                system("python -m webbrowser -t \"https://google.es/search?q=" + text.replace(" ", "+") + "\"")
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")

            case _:
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")

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

        case "shortcut":
            Keyboard.press(Key.ctrl)
            Keyboard.press(Key.alt)
            Keyboard.press(Key.shift)
            Keyboard.press("a")
            Keyboard.release(Key.ctrl)
            Keyboard.release(Key.alt)
            Keyboard.release(Key.shift)
            Keyboard.release("a")

        case "show":
            osd.show()

        case "hide":
            osd.hide()

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
