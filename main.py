import ast

f = open("test.txt","w+")
f.write("obamaphone\n"
        "sussy baka phone!\n"
        "amogus phone even!\n"
        "bruh\n"
        "agamsilist = [obama, sussy, amogus]")

f = open("test.txt","r")

pi = [line for line in f]

print(pi[4])



list = eval(pi[4])

print(list)