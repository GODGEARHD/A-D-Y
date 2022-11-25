#!/usr/bin/python

import esES
import enUS
from os import name
if name == "nt":
    import wmi
    import osd
from sys import exit

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
                returned = esES.initial(True)
                print(returned)

            case line if line[11:-1] == "'en-US'":
                returned = enUS.initial(True)
                print(returned)
            case _:
                print(line[11:-1])

        while True:
            match returned:
                case "spanish":
                    returned = esES.initial(True)

                case "english":
                    returned = enUS.initial(True)

                case _:
                    if name == "nt":
                        osd.end()
                    exit()
                    return "exit"


main()
