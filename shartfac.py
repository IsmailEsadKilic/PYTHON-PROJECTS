s = int(input("sayı: "))
def fak(d):
    z = 1
    r = 1
    while (z < d):
        r = r * (z+1) # r *= (z+1)
        z = z + 1 # n += 1
    return r
t = fak(s)
print (t)