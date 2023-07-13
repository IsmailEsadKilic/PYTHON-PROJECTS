import math
def Main():
    try:
        print(eval(input("yapmak istedigin islemi gir\n")))
        Main()
    except Exception as e:
        print(e,"bida dene")
        Main()
Main()