import enUS
from modules.keystroke import keystroke
from modules.app import app
from os import system, remove, name as ostype
from playsound import playsound
from gtts import gTTS

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
                enUS.close(icon)
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
