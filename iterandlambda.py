
#iter dersi
agalar = ("aga", "maga", "bruh")
def numerate(sequence,start=0):
    n = start
    for element in sequence:
        yield n, element
        n += 1

for i in numerate(agalar):
    print (i)

print(list((enumerate(agalar))))

for i, j in enumerate (agalar, start=1):
    print(i,j)

#lambda fankşın
double = lambda x: x*2
print(double(5))

volume = lambda a, b, c: a * b * c
print(volume(4,5,6))

author = "tolkienn"
upper = lambda x: x.upper()

print(upper(author))

