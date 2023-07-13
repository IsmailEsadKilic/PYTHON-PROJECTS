import re


def convertstr1(word):
    list1 = []
    list1[:0] = word
    return list1

def convertstr2(word):
    return re.findall('[a-zA-Z]', word)

def convertstr3(word):
    return list(word)



thing = "have you ever played the hit game 'Among Us' ?"
watami = convertstr3(thing)
print(watami)
imataw = watami.copy()
imataw.reverse()
print("".join(imataw))



"""
list1 = ['1', '2', '3', '4']

list2 = list1.copy()

list2.reverse()

print(list1)
print(list2)
"""






