def Main():
    try:
        print(input("yapmak istediğin işlemi gir\n"))
    except:
        print("bida dene")
        Main()
Main()