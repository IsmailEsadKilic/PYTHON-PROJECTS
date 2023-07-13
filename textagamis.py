f = open("text.txt", "a")

f.write("\nCan,100\n")

f = open("text.txt", "r")

for item in f.readlines():
    print(item)


try:
    f = open("agamsı messssiiiiiiiiiii", "r")
except:
    print("agamıs yok")


