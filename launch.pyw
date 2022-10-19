#!/usr/bin/python

import esES
import enUS
from os import name
if name == "nt":
    import wmi

running = False

if name == "nt":
    sao = wmi.WMI()
    for process in sao.Win32_Process():
        if "SAO Utils.exe" == process.Name:
            running = True
            break


def main():
    if name == "nt":
        config = ".\\config.ini"
    else:
        config = "./config.ini"
    with open(config, "r") as file:
        line = file.readlines()
        match line[0]:
            case line if line[11:-1] == "'es-ES'":
                returned = esES.initial(running)
                print(returned)

            case line if line[11:-1] == "'en-US'":
                returned = enUS.initial(running)
                print(returned)
            case _:
                print(line[11:-1])

        while True:
            match returned:
                case "spanish":
                    returned = esES.initial(running)

                case "english":
                    returned = enUS.initial(running)

                case _:
                    return "exit"


"""t2 = threading.Thread(target=main)
t2.daemon = True
t2.start()
while True:
    if t2.is_alive():
        time.sleep(0.1)
        continue
    else:
        exit()"""
main()
