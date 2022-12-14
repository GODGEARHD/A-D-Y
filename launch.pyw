#!/usr/bin/python
import os, esES, enUS, signal, psutil
if os.name == "nt":
    import wmi, osd
from sys import exit

running = False

if os.name == "nt":
    sao = wmi.WMI()
    for process in sao.Win32_Process():
        if "SAO Utils.exe" == process.Name:
            running = True
            break

    pids = []
    for proc in psutil.process_iter():
        if "A-D-Y" in proc.name():
            pids.append(proc.pid)
    for pid in pids:
        if pid != os.getpid():
            os.kill(pid, signal.SIGINT)
        else:
            continue


def main():
    if os.name == "nt":
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
                    if os.name == "nt":
                        osd.end()
                    exit()
                    return "exit"

main()
