import esES
import enUS

returned = None

with open("./config.ini", "r") as file:
    for line in file:
        match line:
            case line if line[11:-1] == "'es-ES'":
                returned = esES.__init__()
                print(returned)
            case line if line[11:-1] == "'en-US'":
                returned = enUS.__init__()
                print(returned)

    while True:
        if returned == "spanish":
            returned = esES.__init__()

        elif returned == "english":
            returned = enUS.__init__()
