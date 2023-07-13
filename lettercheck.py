def main1():
    text = "hello World"[::-1]
    #In this particular example, the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.
    print(text)

def main2 (word1,word2):
    #checks if one letter of a word is in another
    for letter in word1:
        if letter in word2:
            print(letter)

#main2("haveyoueverplayedthegameamogus","lilmoseyiswhitesussyballs")
main1()


