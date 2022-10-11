from sys import exit
import esES
import enUS
import wmi
import threading
from pystray import MenuItem as item
import pystray
from PIL import Image


def action():
    pass


def close(icon):
    icon.stop()


def tray(lang):
    menu = None
    image = Image.open("..\\LOGO-ADY.png")
    if lang == "spanish":
        menu = (item('A-D-Y en ejecución...', action, visible=False), item('Salir', lambda: close(icon), visible=False))
    elif lang == "english":
        menu = (item('A-D-Y running...', action, visible=False), item('Exit', lambda: close(icon), visible=False))
    icon = pystray.Icon("name", image, "A-D-Y", menu)
    icon.run()
    return "exit"


running = False

sao = wmi.WMI()
for process in sao.Win32_Process():
    if "SAO Utils.exe" == process.Name:
        running = True
        break


def second():
    with open(".\\config.ini", "r") as file:
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
    with open(".\\config.ini", "r") as file:
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
                    exit()


t1 = threading.Thread(target=second)
t1.daemon = True
t1.start()
main()
