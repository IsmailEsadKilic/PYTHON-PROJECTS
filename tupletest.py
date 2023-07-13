"""
li = [4234234,657,6,66,56,6,64,6,3,3366,5656565,66,56,54665656,45656,56,556546565,565656565656,]
def di (x):
    return x/10
li.sort(key=di,reverse=True)
print(li)

tu = tuple(li)
print(tu)
print(type(tu))

print(list("things"))

t = ("A",) + tu[1:]
print(t)

a = 1
b = 2

a,b = b,a

print(a)
print(b)

obama = "obama hamburger sussy bruh"
obama.split(sep=" ")
print(obama)
care = obama.split(sep=" ")
print(care)
print(type(care))

tupaq = ("kü","we")
print(type(tupaq))
w,q = tupaq
print(w)
print(q)

def ohatuplelarcokhavali(t):
    li = t.split(sep=" ")
    return li[1], li[2], li[3], li[0]

print(ohatuplelarcokhavali(obama))
"""

"""
def func(aga1=None, aga2=None, aga3=None):
    print(aga1, aga2, aga3)

agargs = [2, 2, 3]
kagargs = {"aga2":2,"aga1":1,"aga3":3}

func(**kagargs)
"""

