from os import system


def volume(action, amount):
    match action:
        case "set":
            result = system("setvol " + str(amount))
            print(result)
            if result != 0:
                return True
            else:
                return False
        case "inc":
            result = system("setvol +" + str(amount))
            print(result)
            if result != 0:
                return True
            else:
                return False
        case "dec":
            result = system("setvol -" + str(amount))
            print(result)
            if result != 0:
                return True
            else:
                return False
        case _:
            return True
