def returner(until):
    z = 0
    text = ""
    while z <= until:
        if z % 3 == 0 and z % 5 == 0:
            text = text + str(z) + "üç ve beş\n"
        elif z % 3 == 0:
            text = text + str(z) + "üç\n"
        elif z % 5 == 0:
            text = text + str(z) + "beş\n"
        else:
            text = text + str(z) + "\n"
        z = z + 1
    return text

s = returner(int(input("sayı: ")))
print(s)








#everyone is their own judge
#everyone is their own teacher