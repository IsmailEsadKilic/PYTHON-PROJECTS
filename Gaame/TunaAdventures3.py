import pickle
import os

class tile(): #types are:sea, alien_jungle, treasure_beach, bandit_jungle, jungle,
              # beach, town, tribe_jungle, volcano, treasure_jungle, palm, shipwrech_beach
    def __init__(self,x,y,type):
        self.location = (int(x), int(y))
        self.type = str(type)

class sea(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "sea"

class alien_jungle(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "alien_jungle"

class treasure_beach(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "treasure_beach"

class bandit_jungle(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "bandit_jungle"

class jungle(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "jungle"

class beach(tile):
    def __init__(self, x, y):
        self.location = (int(x), int(y))
        self.type = "beach"

class town(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "town"

class tribe_jungle(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "tribe_jungle"

class volcano(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "volcano"

class treasure_jungle(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "treasure_jungle"

class palm(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "palm"

class shipwreck_beach(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "shipwreck beach"

class item():
    def __init__(self,tpye,name):
        self.name = str(name)
        self.tpye = str(tpye)

class weapon(item):
    def __init__(self,name,dmg):
        self.name = str(name)
        self.tpye = "weapon"
        self.damage = int(dmg)

class consumable(item):
    def __init__(self,name,bonushp):
        self.name = str(name)
        self.type = "consumable"
        self.bonushp = int(bonushp)

class player():
    sword = weapon("sword",5)
    whiskey = consumable("whiskey",40)
    musket = weapon("musket",10)
    bullet = item("bullet","bullet")
    coin = item("coin","coin")

    default_items = [sword,whiskey,whiskey,whiskey,musket,bullet,bullet,bullet,bullet,bullet,
                     coin,coin,coin,coin,coin,coin,coin,coin,coin,coin,coin,coin,coin,coin,coin,coin]

    def __init__(self,hp=100,name="obama",items=default_items,location=[2,3]):
        self.hp = int(hp)
        self.name = str(name)
        self.item = list(items)
        self.playerlocation = list(location)

def startgame(): #returns the first choice and the directory
    print("welcome to TUNA ADVENTURES 3 !")
    print("type the number of the option you want to choose:\n"
          "1 : New Game\n"
          "2 : Load Game\n"
          "3 : Settings\n"
          "4 : Exit Game\n")
    menu_choice, directory = int(input("Select: ")), os.getcwd()
    if menu_choice == 1:
        newsavename = input("Create a new save called: ")
        if newsavename == "":
            CreateNewSave()
        else:
            CreateNewSave(newsavename)
        return startgame()

    if menu_choice == 2:
        if CountSaves() == 0:
            newsavename = input("You have no saves! Create a new save called: ")
            if newsavename == "":
                CreateNewSave()
            else:
                CreateNewSave(newsavename)

        print("your saves are:")
        savelist = ListSaves()
        for item in savelist:
            print(f"{savelist.index(item) + 1} : {item}")
        load_choice = int(input("select 0 to return. Select: "))
        if load_choice == 0:
            return startgame()
        else:
            return load_choice - 1

    if menu_choice == 3:
        print("we dont have settings yet! ¯\_(ツ)_/¯")
        return startgame()
    if menu_choice == 4:
        return "exitgame"

def ListSaves(): #lists the saves and returns
    list = os.listdir(f"{os.getcwd()}\playerdata")
    return list

def CountSaves():
    dir_path = f"{os.getcwd()}\playerdata"
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count

def CreateNewSave(savename=f"save{str(CountSaves() + 1)}"):
    fullsavename = os.getcwd() + f"\playerdata\{savename}"
    try:
        open(f"{fullsavename}.txt", "x")
        with open(f"{fullsavename}.txt","wb") as file:
            pickle.dump()

    except FileExistsError:
        savename = input(f"A save called {savename} already exists! Try another name:")
        CreateNewSave(savename)

def PlaySave(map,character,):
    print("\n\n")

def turn(map,):
    pass


def main():
    menu_output = startgame()
    if menu_output == "exitgame":
        print("\nthanks for playing and see you later!\n")
        return None
    elif menu_output == "s":
        return None
    elif isinstance(menu_output,int):
        print("\nGAME BEGINS!\n")
        f = open(f"{os.getcwd()}\playerdata\{ListSaves()[menu_output]}","w+")
        if f.read() == "":
            f.write("map\n"
                    "")
        playsave_return = PlaySave()
        if playsave_return == "backtomenu":
            main()
        return None
    else:
        print("wtf?")
        return None

"""
defaultmap =[[alien_jungle(), sea, sea, sea, sea, sea, sea, treasure_beach],
             [sea, sea, bandit_jungle, jungle, sea, volcano, sea, sea],
             [sea, sea, beach, town, sea, tribe_jungle, sea, sea],
             [sea, sea, sea, sea, sea, sea, sea, sea],
             [sea, shipwreck_beach, sea, sea, palm, sea, sea, treasure_jungle]

defaultmap = [A1]
main()
"""

sword = weapon
with open("objdata.txt","wb") as file:
    pass