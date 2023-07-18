#dont be so mad
def dontBeMad(you):
    if you.mad:
        print("don't be so mad")
        you.mad = False

class you:
    def __init__(self):
        self.mad = True
    
you = you()
print("are you mad?")
print(you.mad)

dontBeMad(you)
print("are you mad?")
print(you.mad)

# Path: CommentHell.py
import os
#who made this
def whoMadeThis():
    print("who made this")
    #find out who made this
    os.system("git log -1 --pretty=format:'%an'")
    #find out when this was made
    os.system("git log -1 --pretty=format:'%ad'")
    #find out what was the last commit
    os.system("git log -1 --pretty=format:'%s'")

whoMadeThis()