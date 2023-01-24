from os import name as ostype, popen


def app(program):
    if ostype == "nt":
        path = "\".\\programs\\" + program + ".lnk\""
        popen(path)
    else:
        pass
