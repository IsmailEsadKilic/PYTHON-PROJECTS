#check for palindrom
num = str(input("number: "))

def check(num):
    list1 = list(num)
    list1.reverse()
    if list1 == list(num):
        return "ya"
    else:
        return "no"

print(check(num))

