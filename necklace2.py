def necklace2(word):
    return "".join([str(i % 2) for i in range(1,len(word)+1)])
print(necklace2("obama"))