import esES
import enUS
import wmi

returned = None

running = False

sao = wmi.WMI()
for process in sao.Win32_Process():
    if "SAO Utils.exe" == process.Name:
        running = True
        break

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
        if returned == "spanish":
            returned = esES.__init__(running)

        elif returned == "english":
            returned = enUS.__init__(running)
