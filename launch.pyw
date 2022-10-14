#!/usr/bin/python

import time
from sys import exit
import esES
import enUS
import threading
from pystray import MenuItem as item
import pystray
from PIL import Image
from os import name
if name == "nt":
    import wmi


def action():
    pass


def close(icon):
    icon.stop()


def tray(lang):
    icon = None
    if name == "nt":
        image = Image.open(".\\LOGO-ADY.png")
    else:
        image = Image.open("./LOGO-ADY.png")
    if lang == "spanish":
        menu = (item('Change to: English', action, visible=False), item('Salir', lambda: close(icon), visible=True))
        icon = pystray.Icon("name", image, "A-D-Y en ejecución...", menu)
    elif lang == "english":
        menu = (item('Cambiar a: Español', action, visible=False), item('Exit', lambda: close(icon), visible=True))
        icon = pystray.Icon("name", image, "A-D-Y running...", menu)
    icon.run()
    return "exit"


running = False

if name == "nt":
    sao = wmi.WMI()
    for process in sao.Win32_Process():
        if "SAO Utils.exe" == process.Name:
            running = True
            break


def second():
    if name == "nt":
        config = ".\\config.ini"
    else:
        config = "./config.ini"
    with open(config, "r") as file:
        for line in file:
            match line:
                case line if line[11:-1] == "'es-ES'":
                    returned = tray("spanish")
                    print(returned)
                case line if line[11:-1] == "'en-US'":
                    returned = tray("english")
                    print(returned)

        while True:
            match returned:
                case "spanish":
                    returned = tray("spanish")

                case "english":
                    returned = tray("english")

                case _:
                    return "exit"


def main():
    if name == "nt":
        config = ".\\config.ini"
    else:
        config = "./config.ini"
    with open(config, "r") as file:
        for line in file:
            match line:
                case line if line[11:-1] == "'es-ES'":
                    returned = esES.__init__(running)
                    print(returned)

                case line if line[11:-1] == "'en-US'":
                    returned = enUS.__init__(running)
                    print(returned)

        while True:
            match returned:
                case "spanish":
                    returned = esES.__init__(running)

                case "english":
                    returned = enUS.__init__(running)

                case _:
                    return "exit"


t1 = threading.Thread(target=second)
t1.daemon = True
t1.start()
t2 = threading.Thread(target=main)
t2.daemon = True
t2.start()
while True:
    if t1.is_alive() and t2.is_alive():
        time.sleep(0.1)
        continue
    else:
        exit()
