import requests
from playsound import playsound
from time import sleep
from os import name as ostype


def check():
    for i in range(5):
        try:
            requests.get("https://www.google.com", timeout=1)
        except (requests.ConnectionError, requests.Timeout):
            if i == 4:
                print("Sin conexión a internet.")
                audio = "Vaya, parece que no tienes conexión a internet. Para poder funcionar correctamente, " \
                        "necesito que primero te conectes a la red."
                print(audio)
                if ostype == "nt":
                    playsound(".\\esES\\noInternet.mp3")
                else:
                    playsound("./esES/noInternet.mp3")
                return False
            else:
                i += 1
                sleep(1)
                continue
        else:
            print("Con conexión a internet.")
            return True
