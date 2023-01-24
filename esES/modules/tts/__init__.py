import esES
from modules.keystroke import keystroke
from modules.app import app
from modules.volume import volume
from os import system, remove, name as ostype
from playsound import playsound
from gtts import gTTS
from sys import exit

mayus_notifier = None
mayus_audio = None
exiting = None
icon = None


def main(notifier_orig, audio_orig, exiting_orig, icon_orig, audio, name, isprogram, text, run):
    global mayus_notifier
    global mayus_audio
    global exiting
    global icon
    mayus_notifier = notifier_orig
    mayus_audio = audio_orig
    exiting = exiting_orig
    icon = icon_orig
    tts(audio, name, isprogram, text, run)


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
                esES.close(icon)
                return "english"

            case "search":
                system("python -m webbrowser -t \"https://google.es/search?q=" + text.replace(" ", "+") + "\"")
                if run:
                    keystroke("hide", run)
                    if ostype == "nt":
                        playsound(".\\audio\\windowHide.wav")
                    else:
                        playsound("./audio/windowHide.wav")

            case "volume":
                text = text.split(" ")
                action = text[0]
                amount = text[1]
                print(action)
                print(amount)
                volume(action, amount)
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

    except Exception as e:
        print(e)
        pass
