from enUS.modules import tts
from playsound import playsound
from modules.keystroke import keystroke
from os import name as ostype
# from time import sleep
import locale, speech_recognition as sr
from datetime import datetime
# from modules import math as sm

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
        myText = r.recognize_google(audio, language='en-US')
    except Exception:
        if run:
            keystroke("", run)
        pass
    myText = myText + " "
    print(myText)
    if ostype == "nt":
        playsound(".\\audio\\stopListen.wav")
    else:
        playsound("./audio/stopListen.wav")

    match myText:

        case myText if "what's up dog " in myText:
            answer = "Yo! Wassup?"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "", False, "", run)

        case myText if "f*** you b**** " in myText or "shut your b**** ass up " in myText \
                       or "fuck you bitch " or "shut your bitch ass up ":
            answer = "Ah nigga don't hate me cuz I'm beautiful nigga. Maybe if you got rid of that old geegee ass " \
                     "haircut you'd got some bitches on your dick. Oh, better yet, maybe Tanisha'll call your dog " \
                     "ass if she ever stop fucking with that brain surgeon or lawyer she fucking with. Niggaaa"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "", False, "", run)

        case myText if "shut yourself down " in myText:
            answer = "All right, if you need something from me, just tap the green button on the top left corner " \
                     "in SAO Utils. See you!"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "bye", False, "", run)

        case myText if "shut up " in myText or "cállate " in myText or "nothing " in myText:
            answer = "All right, if you need something just let me know."
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "", False, "", run)

        case myText if "put the music " in myText or "hit play " in myText or "put music " in myText:
            answer = "Okay, playing multimedia"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "play", False, "", run)

        case myText if "stop the music " in myText or "hit pause " in myText:
            answer = "Gucci, pausing multimedia"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "play", False, "", run)

        case myText if "go to the next song " in myText or "pasa a otra canción " in myText or "next song " in myText:
            answer = "Okay, going to the next song in the list"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "next", False, "", run)

        case myText if "go to the previous song " in myText or "put the last song " in myText \
                       or "previous song " in myText:
            answer = "Okay, going back to the previous song"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "previous", False, "", run)

        case myText if "present yourself " in myText or "who are you " in myText:
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
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "presentation", False, "", run)

        case myText if "power off the PC " in myText or "power off the computer " in myText \
                       or "power off the system " in myText or "power off the session" in myText:
            answer = "Okay, powering off the PC. See you when you turn it on again!"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "", False, "", run)

        case myText if "restart the PC " in myText or "restart the computer " in myText \
                       or "restart the system " in myText or "restart the session" in myText:
            answer = "Right I'm gonna restart your PC. Wait till I do it, it'll be just a moment."
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "reboot", False, "", run)

        case myText if "lock the PC " in myText or "lock the computer " in myText \
                       or "lock the system " in myText or "lock the session" in myText:
            answer = "Locking the PC's session..."
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "lock", False, "", run)

        case myText if "put the PC to sleep " in myText or "put the computer to sleep " in myText \
                       or "put the system to sleep " in myText or "put the session to sleep" in myText:
            answer = "Okay, putting the system in sleep mode."
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "suspend", False, "", run)

        case myText if "search in google " in myText or "search in Google " in myText:
            answer = "Vale, espera que lo busco y te lo enseño"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "search", False, myText[17:-1], run)

        case myText if "tell me the time " in myText or "what time is it " in myText:
            date = datetime.now()
            answer = "Right now, it's " + date.time().strftime("%H:%M")
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "", False, "", run)

        case myText if "tell me the date " in myText or "what day is it today " in myText:
            locale.getlocale()
            date = datetime.now()
            answer = "Today is " + date.date().strftime("%A, %d of %B, %Y")
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "", False, "", run)

        case myText if "switch to Spanish " in myText or "change to Spanish " in myText or "cambia español " in myText \
                       or "cambia a español " in myText:
            # answer = "Okay, switching main program's language to: Spanish"
            answer = "I'm sorry, but I have this voice command function disabled because of a minor bug. If you want " \
                     "to change language, please use the tray icon."
            return tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "language", False, "", run)

        case myText if "open " in myText:
            answer = "Okay, opening " + myText[5:-1]
            tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, myText[5:-1], True, "", run)

        case myText if "increase " in myText and (" volume " in myText or " sound " in myText or
                                                  " the volume " in myText or " the sound " in myText):
            split = myText.split(" ")
            amount = None
            for i in split:
                try:
                    amount = int(i)
                except Exception:
                    continue
            if amount != 1:
                respuesta = "Okay, increasing volume in " + str(amount) + " points"
            else:
                respuesta = "Okay, increasing volume in " + str(amount) + " point"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "volume", False, {"inc", amount}, run)

        case myText if "decrease " in myText and (" volume " in myText or " sound " in myText or
                                                  " the volume " in myText or " the sound " in myText):
            split = myText.split(" ")
            amount = None
            for i in split:
                try:
                    amount = int(i)
                except Exception:
                    continue
            if amount != 1:
                respuesta = "Okay, decreasing volume in " + str(amount) + " points"
            else:
                respuesta = "Okay, decreasing volume in " + str(amount) + " point"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "volume", False, {"dec", amount}, run)

        case myText if ("set at " in myText or "set " in myText) and \
                       (" volume at " in myText or " sound at " in myText or
                        " the volume " in myText or " the sound " in myText):
            split = myText.split(" ")
            amount = None
            for i in split:
                try:
                    amount = int(i)
                except Exception:
                    continue
            if amount != 1:
                respuesta = "Okay, setting volume at " + str(amount) + " points"
            else:
                respuesta = "Okay, setting volume at " + str(amount) + " point"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "volume", False, {"set", amount}, run)

        case myText if "mute all sounds" in myText or "quit all sounds " in myText:
            respuesta = "Okay, muting all sounds"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "volume", False, {"set", "mute"}, run)

        case myText if "unmute all sounds" in myText or "resume all sounds " in myText:
            respuesta = "Okay, unmuting all sounds"
            tts.main(mayus_notifier, mayus_audio, exiting, icon, respuesta, "volume", False, {"set", "unmute"}, run)

        case _:
            if active and myText != " ":
                answer = "what the fuck? what did you say?"
                tts.main(mayus_notifier, mayus_audio, exiting, icon, answer, "error", False, myText, run)
