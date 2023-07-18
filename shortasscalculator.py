import math
def Main():
    try:
        print(eval(input("yapmak istedigin islemi gir\n")))
        Main()
    except Exception as e:
        print(e,"bida dene")
        Main()
Main()

#advice: don't use eval
#it's dangerous
#why?
#because it can run any code
#like what?
#like this:
#eval("import os;os.system('rm -rf /')")
#what does that do?
#it deletes all your files

#how do i make a calculator without eval?
#you can use the ast module
#like this:
