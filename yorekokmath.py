from math import sqrt as kurt
#AAAAAAAAAAAAAAAAAAAAAAAAAAA
x = "global x"

def test():
    global x
    x = "local x"
    print(x)

print(x)
test()
print(x)

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
def outer():
    a = "outer"

def aga():
    print("aga")
    def maga():
        print("maga")
    maga()

aga()
#AAAAAAAAAAAAAAAAAAAAAAAAAA
print(kurt(16))
#AAAAAAAAAAAAAAAAAAAAAAAAAA
def agamsı():
    print("1")
agamsı()
def agamsı():
    print("2")
agamsı()
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
def add(*args):
    return sum(args)
print(add(23,24,2323,1231,123))

def currency_conv(**kwargs):
    print(kwargs)

print(currency_conv(usd=18,euro=19,gbp=22))
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
numbers =[2,4,6,8,10]
def square(n):
    return n * n

yorekok = map(square, numbers)
print("yorekok",list(yorekok))
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
numero = [1,2,3,4,5,6,7,8,9,10]
def check(number):
    if number % 2 == 0:
        return True
    else:
        return False

even_numbers = filter(check,numero)
print(next(even_numbers))
print(list(even_numbers))
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
list1 = ["uno","dos","tres"]
list2 = [1,2]
listimsi = zip(list1,list2)
print(listimsi)
from multtable import mult_table
mult_table()

from parameterstest import test
test()
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
