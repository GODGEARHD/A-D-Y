from esES.modules import tts
from playsound import playsound
from modules.keystroke import keystroke
from os import name as ostype
from time import sleep
import locale, speech_recognition as sr
from datetime import datetime
from modules import math as sm

r = sr.Recognizer()
mayus_notifier = None
mayus_audio = None
exiting = None
icon = None


def main(notifier_orig, audio_orig, exiting_orig, icon_orig, audio, active, run):
    global mayus_notifier
    global mayus_audio
    global exiting
    global icon
    mayus_notifier = notifier_orig
    mayus_audio = audio_orig
    exiting = exiting_orig
    icon = icon_orig
    playback(audio, active, run)


def playback(audio, active, run):
    global mayus_notifier
    global mayus_audio
    global exiting
    global icon
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
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "", False, "", run)

        case myText if "me cago en tu madre " in myText or "mecagoentuputamadre " in myText:
            respuesta = "Y yo en la tuya que se me abre hijueperra"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "", False, "", run)

        case myText if "apágate " in myText:
            # respuesta = "Vale, si necesitas algo de mí, toca el botón verde que tienes arriba a la izquierda en " \
            #            "sao utils. ¡Nos vemos!"
            respuesta = "Vale. Si me necesitas de nuevo, simplemente vuelve a ejecutarme. ¡Nos vemos!"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "bye", False, "", run)

        case myText if "calla " in myText or "cállate " in myText or "nada " in myText:
            respuesta = "Vale, si necesitas algo avísame"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "", False, "", run)

        case myText if "pon la música " in myText or "dale al play " in myText or "pon música " in myText:
            respuesta = "Vale, reproduciendo multimedia"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "play", False, "", run)

        case myText if "para la música " in myText or "dale al pause " in myText:
            respuesta = "Gucci, pausando multimedia"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "play", False, "", run)

        case myText if "pasa otra canción " in myText or "pasa a otra canción " in myText \
                       or "siguiente canción " in myText:
            respuesta = "Vale, pasando a la siguiente canción en la lista de reproducción"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "next", False, "", run)

        case myText if "vuelve una canción hacia atrás " in myText or "pon la última canción " in myText \
                       or "canción anterior " in myText:
            respuesta = "Okay, vuelvo a la canción anterior"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "previous", False, "", run)

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
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "presentation", False, "", run)

        case myText if "apaga el PC " in myText or "apaga el ordenador " in myText or "apaga el equipo " in myText \
                       or "apaga el sistema " in myText or "apaga la sesión" in myText:
            respuesta = "Vale, voy a apagar tu ordenador. ¡Nos vemos cuando lo vuelvas a encender!"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "shutdown", False, "", run)

        case myText if "reinicia el PC " in myText or "reinicia el ordenador " in myText \
                       or "reinicia el equipo " in myText or "reinicia el sistema " in myText \
                       or "reinicia la sesión" in myText:
            respuesta = "De una, voy a reiniciar tu ordenador. Espera mientras lo hago, no tardo nada."
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "reboot", False, "", run)

        case myText if "bloquea el PC " in myText or "bloquea el ordenador " in myText \
                       or "bloquea el equipo " in myText or "bloquea el sistema " in myText \
                       or "bloquea la sesión" in myText:
            respuesta = "Bloqueando sesión del PC..."
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "lock", False, "", run)

        case myText if "suspende el PC " in myText or "suspende el ordenador " in myText \
                       or "suspende el equipo " in myText or "suspende el sistema " in myText \
                       or "suspende la sesión" in myText:
            respuesta = "Okay, poniendo el sistema en modo suspensión."
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "suspend", False, "", run)

        case myText if "busca en google " in myText or "busca en Google " in myText:
            respuesta = "¿Qué quieres que busque exactamente?"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "", False, "", False)
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
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "search", False, myText, run)
            # myText[16:-1]

        case myText if "dime la hora " in myText or "qué hora es " in myText:
            date = datetime.now()
            respuesta = "La hora actual es " + date.time().strftime("%H:%M")
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "", False, "", run)

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
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "", False, "", run)

        case myText if "cambia inglés " in myText or "cambia a inglés " in myText or "change to English " in myText \
                       or "switch to English " in myText:
            # respuesta = "Vale, cambiando el idioma del programa principal a: Inglés"
            respuesta = "Lo siento, pero he dejado la función de cambio de idioma mediante comando de voz " \
                        "temporalmente desactivada por un pequeño bug que encontré hace un rato. Si quieres cambiar " \
                        "el idioma, por favor usa el icono que tienes en tu bandeja del sistema."
            return tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "language", False, "", run)

        case myText if "calcula " in myText or "calcula esto " in myText:
            respuesta = "¿Cuál es la operación?"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "", False, "", False)
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
            result = sm.getResult(myText, "esp")
            if result != "Unable to evaluate equation":
                tts.main(mayus_notifier, mayus_audio, exiting, icon, result, "calc", False, "", run)
            else:
                respuesta = "Oye, creo que te has equivocado al decirme la ecuación, no soy capaz de resolverla. " \
                            "Revísala y dímela otra vez."
                tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "calc", False, "", run)

        case myText if "abre " in myText:
            respuesta = "okay, abriendo " + myText[5:-1]
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, myText[5:-1], True, "", run)

        case myText if "sube " in myText and (" el volumen " in myText or " el sonido " in myText):
            split = myText.split(" ")
            amount = None
            for i in split:
                try:
                    amount = int(i)
                except Exception:
                    continue
            if amount != 1:
                respuesta = "Vale, subo el volumen " + str(amount) + " puntos"
            else:
                respuesta = "Vale, subo el volumen " + str(amount) + " punto"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "volume",
                     False, ("inc " + str(amount)), run)

        case myText if "baja " in myText and (" el volumen " in myText or " el sonido " in myText):
            split = myText.split(" ")
            amount = None
            for i in split:
                try:
                    amount = int(i)
                except Exception:
                    continue
            if amount != 1:
                respuesta = "Vale, bajo el volumen " + str(amount) + " puntos"
            else:
                respuesta = "Vale, bajo el volumen " + str(amount) + " punto"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "volume",
                     False, ("dec " + str(amount)), run)

        case myText if ("pon a " in myText or "pon " in myText) and \
                       (" el volumen a " in myText or " el sonido a " in myText or
                        " el volumen " in myText or " el sonido " in myText):
            split = myText.split(" ")
            amount = None
            for i in split:
                try:
                    amount = int(i)
                except Exception:
                    continue
            if amount != 1:
                respuesta = "Vale, pongo el volumen a " + str(amount) + " puntos"
            else:
                respuesta = "Vale, pongo el volumen a " + str(amount) + " punto"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "volume",
                     False, ("set " + str(amount)), run)

        case myText if ("mutea " in myText or "quita " in myText) and \
                       (" el volumen " in myText or " el sonido " in myText):
            respuesta = "Vale, muteo el volumen"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "volume", False, "set mute", run)

        case myText if ("desmutea " in myText or "vuelve a poner " in myText) and \
                       (" el volumen " in myText or " el sonido " in myText):
            respuesta = "Vale, vuelvo a poner el volumen"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "volume", False, "set unmute", run)

        case _:
            if active and myText != " ":
                respuesta = "guatafak? qué has dicho?"
                tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "error", False, myText, run)
