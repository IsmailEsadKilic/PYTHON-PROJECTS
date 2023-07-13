from os import remove
import random

class Amogus:
    def __init__(self, type, color, location, username, sus = False):
        self.type = type
        self.color = color
        self.location = location
        self.sus = sus
        self.username = username
    def isitsus(self):
        if self.sus:
            return "hella sus"
        else:
            return "not sus"

# Possible colors and locations
types = ["impostor", "crewmate"]
colors = ["cyan", "blue", "red", "green", "purple", "pink", "yellow",  "brown", "black", "white"]
locations = ["cafeteria", "admin", "navigation", "communication", "electrical", "engines", "medbay", "laser", "oxygen", "reactor"]
words = ["funny", "cool", "crazy", "awesome", "random", "silly", "wacky", "zany", "amazing", "incredible"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

# Create 10 random Amogus objects
Amogus_list = []
# Generate 4 lists of 10 random numbers
lists = [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]
for i in range(4):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    for a in range(10):
        r = random.randint(0,len(numbers)-1)
        lists[i][a] = numbers[r]
        numbers.remove(numbers[r])
for i in range(10):
        Amogus_list.append(Amogus(random.choice(types), colors[lists[0][i]], locations[lists[1][i]], words[lists[2][i]] + str(random.randint(0,100)) + symbols[lists[3][i]]))
#make em sus

numbers = [0,1,2,3,4,5,6,7,8,9]
r1 = random.randint(0,len(numbers)-1)
numbers.remove(numbers[r1])
r2 = random.randint(0,len(numbers)-1)

Amogus_list[r1].sus = True
Amogus_list[r2].sus = True

for baka in Amogus_list:
    print(f"{baka.color}player: {baka.username} is in {baka.location} and he is {baka.isitsus()}!!!")