import pickle
import os
import turtle

class tile(): #types are:sea, alien_jungle, treasure_beach, bandit_jungle, jungle,
              # beach, town, tribe_jungle, volcano, treasure_jungle, palm, shipwrech_beach
    def __init__(self,x,y,type):
        self.location = (int(x), int(y))
        self.type = str(type)

class sea(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "sea"
        self.explored = False
        self.desc = "Open sea"

class alien_jungle(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "jungle"
        self.explored = False
        self.desc = "A jungle with strange lights"

class treasure_beach(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "island"
        self.explored = False
        self.desc = "A small island shaped like a triangle with no trees"

class bandit_jungle(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "jungle"
        self.explored = False
        self.desc = "A jungle with visible campfire smokes"

class jungle(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "jungle"
        self.explored = False
        self.desc = "A jungle with animals"

class beach(tile):
    def __init__(self, x, y):
        self.location = (int(x), int(y))
        self.type = "beach"
        self.explored = False
        self.desc = "A beach with people"

class town(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "town"
        self.explored = False
        self.desc = "A port town with a marketplace and a castle"

class tribe_jungle(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "jungle"
        self.explored = False
        self.desc = "A jungle with strange people on the beach"

class volcano(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "volcano"
        self.explored = False
        self.desc = "A volcano mountain"

class treasure_jungle(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "jungle"
        self.explored = False
        self.desc = "A jungle with a small rowboat on the shore"

class palm(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "island"
        self.explored = False
        self.desc = "A small island with a few palm trees"

class shipwreck_beach(tile):
    def __init__(self,x,y):
        self.location = (int(x), int(y))
        self.type = "island"
        self.explored = False
        self.desc = "An island with a shipwreck on it"

class item():
    def __init__(self,tpye,name):
        self.name = str(name)
        self.type = str(tpye)

class weapon(item):
    def __init__(self,name,dmg):
        self.name = str(name)
        self.type = "weapon"
        self.damage = int(dmg)

class consumable(item):
    def __init__(self,name,bonushp):
        self.name = str(name)
        self.type = "consumable"
        self.bonushp = int(bonushp)

    def useininventory(self,player):
        print(f"you used the {self.name}!")
        player.hp += self.bonushp
        if player.hp > 100:
            player.hp = 100
        player.items.remove(self)


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
        self.items = list(items)
        self.playerlocation = list(location)

A1 = alien_jungle(0,0)
A2 = sea(0,1)
A3 = sea(0,2)
A4 = sea(0,3)
A5 = sea(0,4)
A6 = sea(0,5)
A7 = sea(0,6)
A8 = treasure_beach(0,7)
B1 = sea(1,0)
B2 = sea(1,1)
B3 = bandit_jungle(1,2)
B4 = jungle(1,3)
B5 = sea(1,4)
B6 = sea(1,5)
B7 = volcano(1,6)
B8 = sea(1,7)
C1 = sea(2,0)
C2 = sea(2,1)
C3 = beach(2,2)
C4 = town(2,3)
C5 = sea(2,4)
C6 = sea(2,5)
C7 = tribe_jungle(2,6)
C8 = sea(2,7)
D1 = sea(3,0)
D2 = sea(3,1)
D3 = sea(3,2)
D4 = sea(3,3)
D5 = sea(3,4)
D6 = sea(3,5)
D7 = sea(3,6)
D8 = sea(3,7)
E1 = sea(4,0)
E2 = shipwreck_beach(4,1)
E3 = sea(4,2)
E4 = sea(4,3)
E5 = palm(4,4)
E6 = sea(4,5)
E7 = sea(4,6)
E8 = treasure_jungle(4,7)

defaultmap = [[A1, A2, A3, A4, A5, A6, A7, A8],
             [B1, B2, B3, B4, B5, B6, B7, B8],
             [C1, C2, C3, C4, C5, C6, C7, C8],
             [D1, D2, D3, D4, D5, D6, D7, D8],
             [E1, E2, E3, E4, E5, E6, E7, E8]]

defaultchar = player()

def explore(map,player):
    j, k = player.playerlocation[0], player.playerlocation[1]
    for a in range(5):
        for b in range(8):
            if (map[a][b].explored == False) and ((a == j or a == j-1 or a == j+1) and (b == k or b == k-1 or b == k+1)):
                map[a][b].explored = True

def visualise(map,player):
    uimap =[[],[],[],[],[]]
    for a in range(5):
        for i in range(8):
            x = map[a][i]
            if not x.explored:
                uimap[a].append(f"          ?              ")
            elif x.explored and player.playerlocation[0] == a and player.playerlocation[1] == i:
                uimap[a].append(f"{x.type} (you)" + " "*(19-len(x.type)))
            elif x.explored:
                uimap[a].append(x.type + " "*(25-len(x.type)))
    for x in range(5):
       print("-"*207+"\n"f"|{uimap[x][0]}|{uimap[x][1]}|{uimap[x][2]}|{uimap[x][3]}|{uimap[x][4]}|"
             f"{uimap[x][5]}|{uimap[x][6]}|{uimap[x][7]}|")
    print("-"*207)

def tellsurrounding(map,player):
    print(f"in the northwest you see: {map[player.playerlocation[0]-1][player.playerlocation[1]-1].desc}")
    print(f"in the north you see: {map[player.playerlocation[0]-1][player.playerlocation[1]].desc}")
    print(f"in the northeast you see: {map[player.playerlocation[0]-1][player.playerlocation[1]+1].desc}")
    print(f"in the west you see: {map[player.playerlocation[0]][player.playerlocation[1]-1].desc}")
    print(f"you are now at: {map[player.playerlocation[0]][player.playerlocation[1]].desc}")
    print(f"in the east you see: {map[player.playerlocation[0]][player.playerlocation[1]+1].desc}")
    print(f"in the southwest you see: {map[player.playerlocation[0]+1][player.playerlocation[1]-1].desc}")
    print(f"in the south you see: {map[player.playerlocation[0]+1][player.playerlocation[1]].desc}")
    print(f"in the southeast you see: {map[player.playerlocation[0]+1][player.playerlocation[1]+1].desc}")
    print(f"\nyour hp is: {player.hp}")

def mapturn(map,player):
    explore(map,player)
    visualise(map,player)
    tellsurrounding(map,player)
    print("\n 8: go north\n 4: go west\n 5: go south\n 6: go east\n\n 1: enter the place you are on\n 2: open inventory\n 0: save and exit")
    return int(input("select: "))

def playsave(map,player):
    running = True
    while running:
        turnchoice = mapturn(map,player)
        if turnchoice == 8:
            player.playerlocation[0] -= 1
        if turnchoice == 4:
            player.playerlocation[1] -= 1
        if turnchoice == 5:
            player.playerlocation[0] += 1
        if turnchoice == 6:
            player.playerlocation[1] += 1
        if turnchoice == 1:
            print("you cant enter yet lol!")
        if turnchoice == 2:
            viewinginventory = True
            while viewinginventory:
                print(f"your items are:")
                i = 1
                for item in player.items:
                    print(f"{i}: {item.name} ({item.type})")
                    i += 1
                print("to use the item, type its index. To return to map, type 0")
                inventorychoice = int(input("select: "))
                if inventorychoice == 0:
                    viewinginventory = False
                else:
                    try:
                        player.items[inventorychoice-1].useininventory(player)
                    except:
                        print("you cant use that!")

        if turnchoice == 0:
            running = False
    return "all the objects should be here"


def startgame(): #returns the first choice and the directory
    print("welcome to TUNA ADVENTURES 3 !")
    print("type the number of the option you want to choose:\n"
          "1 : New Game (dont choose doesnt work yet!)\n"
          "2 : Load Game (dont choose doesnt work yet!\n"
          "3 : Settings (dont choose doesnt work yet!\n"
          "4 : Exit Game\n"
          "5 : PLay the demo\n")
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
        return "s"
    if menu_choice == 4:
        return "exitgame"
    if menu_choice == 5:
        return "demo"

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
        print("we dont have settings yet! ¯\_(ツ)_/¯")
        main()
        return None
    elif menu_output == "demo":
        playsave(defaultmap,defaultchar)
        main()
    elif isinstance(menu_output,int):
        print("we cant load game yet lol!")
        main()
        return None
    else:
        print("wtf?")
        return None

if __name__ == '__main__':
    main()