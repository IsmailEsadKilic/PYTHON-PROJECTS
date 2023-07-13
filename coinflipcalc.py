#16 finder
import random
def get_four_random_bits():
    fi = random.randint(0,1)
    se = random.randint(0,1)
    th = random.randint(0,1)
    fo = random.randint(0,1)
    return [fi , se , th , fo]

def main1(tries):
    succes = 0
    for i in range(0,tries):
       if get_four_random_bits() == [1 , 1 , 1 , 1]:
           succes += 1
       else:
           pass
    return succes / tries * 100

print("chance of succes= " , main1(int(input("input tries: "))), " percent (1/16 = 6.25 %)")








