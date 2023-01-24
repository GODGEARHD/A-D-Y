from math import *


def getEquation(equation):
    """ Replace words (without accents) for mathematical signs. """
    obj = {"cuanto es": "", "how much is": "", "mas": "+", "plus": "+", "menos": "-", "minus": "-", "entre": "/",
           "divided by": "/", "por ": "* ", "times ": "* ", "x": "*", "abre parentesis": "(", "open parentheses": "(",
           "cierra parentesis": ")", "close parentheses": ")", "negativo": "-", "negative": "-", "elevado a la": "**",
           "raised to": "**", "a porcentaje": "", "to percentage": "", "y": "", "and": "", "the": "", "la": "",
           "el": "", "raiz de": "", "square root of": "", "root of": "", ",": ""}
    objKeys = list(obj.keys())
    objValues = list(obj.values())

    for i in range(len(objKeys)):
        if objKeys[i] in equation:
            equation = equation.replace(objKeys[i], objValues[i])
    return equation.strip()


def transformNumbers(equation):
    """
        If the voice gets numbers with letters instead of numbers,
        we replace them here.
    """
    nums = {"cero": "0", "uno": "1", "dos": "2", "tres": "3", "cuatro": "4", "cinco": "5", "seis": "6", "siete": "7",
            "ocho": "8", "nueve": "9", "diez": "10", "once": "11", "doce": "12", "trece": "13", "catorce": "14",
            "quince": "15", "dieciseis": "16", "diecisiete": "17", "dieciocho": "18", "diecinueve": "19",
            "veinte": "20", "veintiuno": "21", "veintidos": "22", "veintitres": "23", "veinticuatro": "24",
            "veinticinco": "25", "veintiseis": "26", "veintisiete": "27", "veintiocho": "28", "veintinueve": "29",
            "treinta": "30", "cuarenta": "40", "cincuenta": "50", "sesenta": "60", "setenta": "70", "ochenta": "80",
            "noventa": "90", "cien": "100", "mil": "1000", "millon": "1000000", "billon": "1000000000",
            "trillon": "1000000000000", "cuatrillon": "1000000000000000", "quintillon": "1000000000000000000",
            "sextillon": "1000000000000000000000", "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10", "eleven": "11",
            "twelve": "12", "thirteen": "13", "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
            "eighteen": "18", "nineteen": "19", "twenty": "20", "thirty": "30", "fourty": "40", "fifty": "50",
            "sixty": "60", "seventy": "70", "eighty": "80", "ninety": "90", "hundred": "100", "thousand": "1000",
            "million": "1000000", "billion": "1000000000", "trillion": "1000000000000",
            "quadrillion": "1000000000000000", "quintillion": "1000000000000000000",
            "sextillion": "1000000000000000000000"}
    numsKeys = list(nums.keys())
    numsValues = list(nums.values())

    eqSplit = equation.split()

    for i in range(len(eqSplit)):
        for j in range(len(numsKeys)):
            if eqSplit[i] == numsKeys[j]:
                eqSplit[i] = eqSplit[i].replace(eqSplit[i], numsValues[j])
                break
    return "".join(eqSplit)


def getResult(equation, lang):
    """ Get result calling other functions. """
    equation = equation.lower()
    equation = equation.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    eq = transformNumbers(getEquation(equation))

    try:
        if "raiz de" in equation or "square root of" in equation or "root of" in equation:
            a = float(eq)
            ev = eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt})

        elif "a porcentaje" in equation or "to percentage" in equation:
            ev = "{:.1%}".format(float(eq))

        else:
            ev = eval(eq)

        if lang == "esp":
            return "El resultado es  {:,d}".format(int(ev))
        elif lang == "eng":
            return "The answer is  {:,d}".format(int(ev))
        else:
            return "XD"
    except Exception:
        if lang == "esp":
            return "Imposible evaluar la ecuación"
        elif lang == "eng":
            return "Unable to evaluate equation"
        else:
            return "XD"


"""cad = list(transformNumbers("Pon el volumen a treinta"))
print(cad)

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u",
       "v", "w", "x", "y", "z"]
for i in range(len(cad)):
    for j in range(len(abc)):
        if cad[i] == abc[j]:
            cad[i].replace(cad[i], abc[j])

print("-----------")
print(cad)"""
