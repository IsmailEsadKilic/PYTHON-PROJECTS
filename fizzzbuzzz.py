def returner(until):
    z = 0
    while (z <= until):
        if z%3 == 0 and z%5 == 0:
            print( z , "üç ve beş")
        elif z%3 == 0:
            print( z , "üç")
        elif z%5 == 0:
            print( z , "beş")
        else:
            print(z)
        z = z + 1
returner(int(input("bi sayı girmelisin: ")))
