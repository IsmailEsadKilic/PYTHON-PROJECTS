def Main():
    try:
        print(input("yapmak istedi�in i�lemi gir\n"))
    except:
        print("bida dene")
        Main()
Main()