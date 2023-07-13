def returner (z):
    if z%2 == 0:
        return "its even"
    elif z%2 == 1:
        return "its odd"
s = returner(int(input("what is it ")))
print (s)




