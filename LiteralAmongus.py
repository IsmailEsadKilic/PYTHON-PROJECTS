import turtle
import math
import random
import time
from math import dist

turt1 = turtle.Turtle()
turt2 = turtle.Turtle()
turt3 = turtle.Turtle()
#class for a room
class Room:
    def __init__(self, name, connectedRooms=[],coords=(400,400)):
        self.name = name
        self.connectedRooms = connectedRooms
        self.coords = coords
        self.bodies = []

cafeteria = Room("Cafeteria",)
weapons = Room("Weapons",)
navigation = Room("Navigation",)
shields = Room("Shields",)
o2 = Room("O2",)
admin = Room("Admin",)
storage = Room("Storage",)
communications = Room("Communications",)
electrical = Room("Electrical",)
#electrical is sus
medbay = Room("Medbay",)
Engine = Room("Engine",)
security = Room("Security",)
reactor = Room("Reactor",)
airlock = Room("Airlock",)
greenhouse = Room("Greenhouse",)
#vent is connected to all rooms and is sus and is off the map at -500,0
vent = Room("Vent",[],(-500,0))
#constructing the random map


roomsWithoutCaf = [weapons, navigation, shields, o2, admin, storage, communications, electrical, medbay, Engine, security, reactor, airlock, greenhouse]
rooms = roomsWithoutCaf.copy()
random.shuffle(rooms)
rooms.insert(7,cafeteria)

roomsmatrix = [[],[],[]]
for i in range(3):
    for a in range(5):
        roomsmatrix[i].append(rooms[i*5+a])

#if room 8 isnt cafeteria, swap it with cafeteria

for i in range(3):
    for a in range(5):
            roomsmatrix[i][a].coords = (-500+a*200,-200+i*200)



def visualize(matrix=roomsmatrix):
    turt1.penup()
    turt1.hideturtle()
    turt1.speed(0)
    turt1.color("black")
    for i in range(3):
        for a in range (5):
            turt1.penup()
            turt1.goto(-500 + a*200,-300 +i*200)
            turt1.pendown()
            turt1.circle(100)
            turt1.write(matrix[i][a].name,font=("Arial", 12, "normal"))
            turt1.dot(10)

#defining the connections between rooms
"""
roomsmatrix[0][0].connectedRooms = [roomsmatrix[0][1],roomsmatrix[1][0]]
roomsmatrix[0][1].connectedRooms = [roomsmatrix[0][0],roomsmatrix[0][2],roomsmatrix[1][1]]
roomsmatrix[0][2].connectedRooms = [roomsmatrix[0][1],roomsmatrix[0][3],roomsmatrix[1][2]]
roomsmatrix[0][3].connectedRooms = [roomsmatrix[0][2],roomsmatrix[0][4],roomsmatrix[1][3]]
roomsmatrix[0][4].connectedRooms = [roomsmatrix[0][3],roomsmatrix[1][4]]
roomsmatrix[1][0].connectedRooms = [roomsmatrix[0][0],roomsmatrix[1][1],roomsmatrix[2][0]]
roomsmatrix[1][1].connectedRooms = [roomsmatrix[0][1],roomsmatrix[1][0],roomsmatrix[1][2],roomsmatrix[2][1]]
roomsmatrix[1][2].connectedRooms = [roomsmatrix[0][2],roomsmatrix[1][1],roomsmatrix[1][3],roomsmatrix[2][2]]
roomsmatrix[1][3].connectedRooms = [roomsmatrix[0][3],roomsmatrix[1][2],roomsmatrix[1][4],roomsmatrix[2][3]]
roomsmatrix[1][4].connectedRooms = [roomsmatrix[0][4],roomsmatrix[1][3],roomsmatrix[2][4]]
roomsmatrix[2][0].connectedRooms = [roomsmatrix[1][0],roomsmatrix[2][1]]
roomsmatrix[2][1].connectedRooms = [roomsmatrix[1][1],roomsmatrix[2][0],roomsmatrix[2][2]]
roomsmatrix[2][2].connectedRooms = [roomsmatrix[1][2],roomsmatrix[2][1],roomsmatrix[2][3]]
roomsmatrix[2][3].connectedRooms = [roomsmatrix[1][3],roomsmatrix[2][2],roomsmatrix[2][4]]
roomsmatrix[2][4].connectedRooms = [roomsmatrix[1][4],roomsmatrix[2][3]]
"""

print(roomsmatrix)
for i in range(3):
    print(roomsmatrix[i][0].name,roomsmatrix[i][1].name,roomsmatrix[i][2].name,roomsmatrix[i][3].name,roomsmatrix[i][4].name)



def AddConnectedRoomsFromTempList(current,templist):
    current.connectedRooms = templist
    for temp in templist:
        print(current.name+ " connected to " + temp.name)
    print(current.name + " has " + str(len(current.connectedRooms)) + " connections")

#defining the connections between rooms

for i in range(3):
    for a in range(5):
        current = roomsmatrix[i][a]
        templist = []
        for b in range(3):
            for c in range(5):
                if abs(b-i)+abs(c-a) == 1:
                    templist.append(roomsmatrix[b][c])
        AddConnectedRoomsFromTempList(current,templist)
    


#printing the connections between rooms
for i in range(3):
    for a in range(5):
        print(roomsmatrix[i][a].name)
        for room in roomsmatrix[i][a].connectedRooms:
            print("    "+room.name)
        print("")
visualize()

#a class for the literal amongi
class Amogus:
    def __init__(self, name, color, location=cafeteria, isImposter=False, inVent=False, killCooldown=2):
        self.name = name
        self.color = color
        self.location = location
        self.isImposter = isImposter
        self.coords = (0,0)
        self.inVent = inVent

#create the players
players = []
players.append(Amogus("Red", "red"))
players.append(Amogus("Blue", "blue"))
players.append(Amogus("Green", "green"))
players.append(Amogus("Yellow", "yellow"))
players.append(Amogus("Orange", "orange"))
players.append(Amogus("Black", "brown"))
players.append(Amogus("Purple", "purple"))
players.append(Amogus("Cyan", "cyan"))
players.append(Amogus("Brown", "brown"))
players.append(Amogus("Lime", "lime"))

random.shuffle(players)
#assign funny internet names
words = ["obama","sussybaker","josegonzales2007","da","baby","big","Chungus","vent","edp446","poggers",
         "litterallyMe","barbenheimer","thugShaker","JohnCena","blockHead","FlightReacts","kys","LoganPaul",
         "MrBeast","PewDiePie","Multiplier","Jacksepticeye","Dream","GeorgeNotFound","Sapnap","AndRotate",
         "theBronzeAge","MissedABeat","Socrates","Plato","Aristotle","NicolasCage","KeanuReeves","Dwayne(rock)j",
         "Dababy","PdfFile","MrEast",]





random.shuffle(words)
for i in range(len(players)):
    players[i].name = words[i]
    print(players[i].name+" ("+players[i].color+")")

#assign the imposters
imposters = []
random.shuffle(players)
players[0].isImposter = True
players[1].isImposter = True
imposters.append(players[0])
imposters.append(players[1])
random.shuffle(players)

print("\nThe imposters are: ")
for imposter in imposters:
    print(imposter.name+" ("+imposter.color+")")
print("")


def TooClose(player,players):
    for otherPlayer in players:
        if otherPlayer != player:
            if dist(player.coords,otherPlayer.coords) < 50:
                return True
    return False

def AmogusPlacer(players):
    for player in players:
        player.coords = (player.location.coords[0]+random.randint(-100,100),player.location.coords[1]+random.randint(-100,100))
        while (dist(player.coords,player.location.coords) > 100 or TooClose(player,players)):
            player.coords = (player.location.coords[0]+random.randint(-100,100),player.location.coords[1]+random.randint(-100,100))
def visualizePlayers(players):
    turt2.penup()
    turt2.hideturtle()
    turt2.speed(0)
    turt2.color("black")
    for player in players:
        turt2.penup()
        turt2.goto(player.coords)
        turt2.pendown()
        turt2.dot(20,player.color)
        turt2.write(player.name,font=("Arial", 12, "normal"))

class deadbody():
    def __init__(self,location,coords,color):
        self.location = location
        self.coords = coords
        self.color = color
    def draw(self):
        turt3.speed(0)
        turt3.penup()
        turt3.goto(self.coords)
        turt3.dot(20,self.color)
        turt3.dot(10,"white")

#can someone explain how amogusplacer works
# takes a list of players and places them in their rooms
# it does this by giving them a random location in the room
# and then checking if they are too close to another player
# or too far from the room
# if they are, it gives them a new location
# it does this until they are in the room and not too close to another player

#why randomize the locations of the players
# so they dont overlap
# and so they arent in the same place every time
# and so they arent in the same place as the room
# and so they arent in the same place as each other

#too much code for something so simple
# i know
#simpler:
"""
def AmogusPlacer(players):
    for player in players:
        player.coords = (player.location.coords[0]+random.randint(-100,100),player.location.coords[1]+random.randint(-100,100))
        while (dist(player.coords,player.location.coords) > 100 or TooClose(player,players)):
            player.coords = (player.location.coords[0]+random.randint(-100,100),player.location.coords[1]+random.randint(-100,100))

def TooClose(player,players):
    for otherPlayer in players:
        if otherPlayer != player:
            if dist(player.coords,otherPlayer.coords) < 50:
                return True
    return False
"""
#how is that simpler
#i removed unnecessary variables
#and made the code more readable
#and removed the comments
#i added the comments back! haha!
#i removed the comments again! haha!

impostersKillCooldown = 2

AmogusPlacer(players)
visualizePlayers(players)

def MoveAmongi(players,imposters,rooms):
    print("Moving players")
    for player in players:
        if player.inVent:
            #if in vent, move to a random room (doesnt need to be connected)
            player.location = random.choice(rooms)
            player.inVent = False


        else:
            #move to a random connected room
            #player.location = random.choice(player.location.connectedRooms)
            #can you make it a 30 percent chance to not move?
            if random.randint(0,100) > 30:
                player.location = random.choice(player.location.connectedRooms)
    AmogusPlacer(players)

def KillAmongi(players,imposters,rooms):
    print("Killing players")
    #if there is 1 crewmate and 1 impostor in a room, kill the crewmate
    for room in rooms:
        crewmates = 0
        impostors = 0
        for player in players:  
            if player.location == room:
                if player.isImposter:
                    impostors += 1
                else:
                    crewmates += 1
        if crewmates <= impostors:
            for player in players:
                if player.location == room:
                    if player.isImposter == False:
                        #deadbody(room,player.coords,player.color) appen to list of dead bodies:
                        body = deadbody(room,player.coords,player.color)
                        body.draw()
                        room.bodies.append(body)
                        players.remove(player)
                        print(player.name+" was killed by an imposter in "+room.name)
                        #set impostors cooldown to 2
                        impostersKillCooldown = 2
                        print("Impostor kill cooldown set to" + str(impostersKillCooldown))

def reportBody(players,imposters,rooms):
    print("Reporting bodies")
    #if there is a body in the room and another crewmate is in, 80 percent chance to, report it, and call a vote
    #currently everyone can report a body, even imposters, which is not how it should be, because why would an imposter report a body.
    for room in rooms:
        if len(room.bodies) > 0:
            for player in players:
                if player.isImposter == False:
                    if player.location == room:
                        if random.randint(0,100) > 20:
                            print(player.name+" reported a body in "+room.name)
                            voteStart(players,imposters,rooms)
                            #this vote says int object is not callable
                            #i think its because you have a variable called vote and a function called vote

def VentAmongi(players,imposters,rooms):
    print("Venting players")
    #30 percent chance to vent
    for player in players:
        if random.randint(0,100) > 70:
            player.inVent = True
            player.location = vent

vote = 0
#make vote a global variable
#i dont know how to do that
#i think you just put global vote at the top of the function

def voteStart(players,imposters,rooms):
    global vote
    turt3.clear()
    #if crewmate, add to the votables once, if imposter, add to the votables twice
    votables = []
    for player in players:
        if player.isImposter:
            votables.append(player)
            votables.append(player)
        else:
            votables.append(player)
    votes = []
    print("Voting players\n")
    print("Who do you think is the imposter?")
    for player in players:
        choice = random.choice(votables)
        print(f"{player.name} ({player.color}) votes for {choice.name} ({choice.color})")
        votes.append(choice)
    remove = random.choice(votes)
    print(f"{remove.name} ({remove.color}) was voted out")
    #tell if they were an imposter or not
    if remove.isImposter:
        print(f"{remove.name} ({remove.color}) was an imposter")
        imposters.remove(remove)
    elif remove.isImposter == False:
        print(f"{remove.name} ({remove.color}) was not a crewmate")
    #remove from players
    players.remove(remove)
    vote += 1
#game loop until there are 2 players left or no imposters left
turn = 0
impostersKillCooldown = 2
while len(players) > 2 and len(imposters) > 0:
    turn += 1
    print("vote "+str(vote))
    print("turn "+str(turn))
    print("There are "+str(len(imposters))+" imposters left")
    print("There are "+str(len(players))+" players left\n")
    turt2.clear()
    visualizePlayers(players)
    time.sleep(1)
    MoveAmongi(players,imposters,rooms)
    turt2.clear()
    visualizePlayers(players)
    time.sleep(1)
    if impostersKillCooldown <= 0:
        KillAmongi(players,imposters,rooms)
    turt2.clear()
    visualizePlayers(players)
    time.sleep(1)
    reportBody(players,imposters,rooms)
    turt2.clear()
    visualizePlayers(players)
    time.sleep(1)
    VentAmongi(players,imposters,rooms)
    turt2.clear()
    visualizePlayers(players)
    time.sleep(1)
        #all impostor cooldowns go down by 1
    impostersKillCooldown -= 1

print("Game over")
if len(imposters) == 0:
    print("Crewmates win")
else:
    print("Imposters win")

turtle.done()

#can there be multiple turtles drawin at the same time? something like multithreading?

#is there a way to ctrl z the turtle? like erase the last drawn shape?
#somethin like turtle.undo()?
#i dont think so
#i think you have to redraw the whole thing
#oh ok
#i think you can do turtle.clear()
#and then redraw everything

"""
#wow this is a lot of code
#who made this?
#it was some guy named "theBronzeAge"
#he must be really cool
#who would make something like this?
#the guy named "theBronzeAge"
#who would call themselves "theBronzeAge"?
#the guy named "theBronzeAge"
#who would make a game like this?
#the guy named "theBronzeAge"
#who would make a game like this and call themselves "theBronzeAge"?
#the guy named "theBronzeAge"
#who would make a game like this and call themselves "theBronzeAge" and make a bunch of comments?
#the guy named "theBronzeAge"
#who would make a game like this and call themselves "theBronzeAge" and make a bunch of comments and then make a bunch of comments about the comments?
#the guy named "theBronzeAge"
#hi im the guy named "theBronzeAge"
#i made this game
#why?
#because i was bored

#young man, kill your self
i eat babies
#yummy
#how do you eat babies?
#with a fork and knife

#why are you still reading this?
#go play the game
#or something
#idk
#bye

#also if you are reading this
#you are a nerd
#go outside
#or something
#idk
#bye

#why did the chicken cross the road?
#to get to the other side
#haha
#funny joke
#ok bye

#ok im done
#bye

#ok im really done
#bye

#ok im really really done
#bye

#hi really really really done im dad

#why did they shuffel the players twice
#i think it was a mistake
#no it wasnt
#it was on purpose
#for:
#reasons

#industrial revolution and its consequences have been a disaster for the human race
#industrial society and its future
#theodore kaczynski
#1995

#kill amongi and vent amongi arent implemented yet

#i think i should stop writing comments
#no!, keep writing comments, they are funny, and i like them, and so does everyone else, so keep writing them please, bronze age.
#does anyone even read these?

#the bronze age sounds a lot like lebron james...
#i wonder if they are related

#i will now write a poem
#roses are red
#violets are blue
#this code is bad
#and so are you

#here is a better one
#roses are red
#violets are blue
#this code is good
#and so are you

#so is the code good or bad?
#i dont know
#i think it is good
#but i am biased
#because i wrote it

#i think i should stop writing comments
#no!, keep writing comments, they are funny, and i like them, and so does everyone else, so keep writing them please, bronze age.
#does anyone even read these?

#i think i should stop writing comments

#really bronze age?
#yes, really
#ok, fine

#add an amongus joke here
#i dont know any amongus jokes
#ok, then add a joke about the bronze age
#ok:
#why did the bronze age cross the road? 
#to get to the other side

#add an amongus joke here:
#there are 2 imposters among us
#haha!

#add bogosort here
def bogosort(list):
    while not isSorted(list):
        random.shuffle(list)
    return list
def isSorted(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

#who added bogosort?
#i did
#why?
#because i can
#ok

#add fastsort here
def fastsort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = []
    right = []
    for i in range(1,len(list)):
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])
    return fastsort(left)+[pivot]+fastsort(right)

#who added fastsort?
#i did
#why?
#because i can
#ok

#how does fastsort work?
#it is recursive
#it splits the list into 2 parts
#the left part is all the elements less than the pivot
#the right part is all the elements greater than or equal to the pivot
#then it sorts the left and right parts
#and then it combines them
#and then it returns the sorted list

#smart
#i know

#does anyone know other sorting algorithms?
#i know one
#what is it?
#merge sort:
def mergesort(list):
    if len(list) <= 1:
        return list
    left = []
    right = []
    for i in range(len(list)):
        if i < len(list)/2:
            left.append(list[i])
        else:
            right.append(list[i])
    left = mergesort(left)
    right = mergesort(right)
    return merge(left,right)
def merge(left,right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result  

#who added mergesort?
#i did
#how does it work?
#it is recursive
#it splits the list into 2 parts
#the left part is the first half of the list
#the right part is the second half of the list
#then it sorts the left and right parts

#difference between mergesort and fastsort?
#mergesort is slower
#but it is more efficient
#because it uses less memory

#time complexity of mergesort?
#O(nlogn)
#fastsort is also O(nlogn)

#time complexity of bogosort?
#O(n*n!)
#it is really bad

#booooooogooooooosooooooort

#i think i should stop writing comments
#no!, keep writing comments, they are funny, and i like them, and so does everyone else, so keep writing them please, bronze age.

#add breadth first search here
#WHAT IS BREADTH FIRST SEARCH?
#BREADTH FIRST SEARCH IS A SEARCH ALGORITHM
#IT IS USED TO FIND THE SHORTEST PATH BETWEEN 2 NODES IN A GRAPH
#IT IS ALSO USED TO FIND THE SHORTEST PATH FROM A NODE TO ALL OTHER NODES IN A GRAPH
#IT IS ALSO USED TO FIND THE SHORTEST PATH FROM ALL NODES TO A NODE IN A GRAPH
#IT IS ALSO USED TO FIND THE SHORTEST PATH FROM ALL NODES TO ALL OTHER NODES IN A GRAPH
#wooooooooooow

def bfs(graph, start):
    visited = []
    queue = [start]
    while len(queue) > 0:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
    return visited

#it would be like this in java:
#public static ArrayList<Integer> bfs(HashMap<Integer,ArrayList<Integer>> graph, int start){
#    ArrayList<Integer> visited = new ArrayList<Integer>();
#    ArrayList<Integer> queue = new ArrayList<Integer>();
#    queue.add(start);
#    while(queue.size() > 0){
#        int node = queue.remove(0);
#        if(!visited.contains(node)){
#            visited.add(node);
#            ArrayList<Integer> neighbors = graph.get(node);
#            for(int neighbor : neighbors){
#                queue.add(neighbor);
#            }
#        }
#    }
#    return visited;
#}

#too much code
#that is why python is better than java
#python is better than java

#it would be like this in c++:
#vector<int> bfs(unordered_map<int,vector<int>> graph, int start){
#    vector<int> visited;
#    vector<int> queue;
#    queue.push_back(start);
#    while(queue.size() > 0){
#        int node = queue[0];
#        queue.erase(queue.begin());
#        if(find(visited.begin(),visited.end(),node) == visited.end()){
#            visited.push_back(node);
#            vector<int> neighbors = graph[node];
#            for(int neighbor : neighbors){
#                queue.push_back(neighbor);
#            }
#        }
#    }
#    return visited;
#}

#too much code
#that is why python is better than c++
#what is better than python?
#nothing

#it would be like this in rust:
#fn bfs(graph: HashMap<i32,Vec<i32>>, start: i32) -> Vec<i32>{
#    let mut visited: Vec<i32> = Vec::new();
#    let mut queue: Vec<i32> = Vec::new();
#    queue.push(start);
#    while queue.len() > 0{
#        let node = queue[0];
#        queue.remove(0);
#        if !visited.contains(&node){
#            visited.push(node);
#            let neighbors = graph.get(&node).unwrap();
#            for neighbor in neighbors{
#                queue.push(*neighbor);
#            }
#        }
#    }
#    return visited;
#}

#too much code
#that is why python is better than rust
#what is better than python?
#nothing

#it would be like this in assembly:
#bfs:
#    push rbp
#    mov rbp,rsp
#    sub rsp,16
#    mov QWORD PTR [rbp-8],rdi
#    mov DWORD PTR [rbp-12],esi
#    mov DWORD PTR [rbp-16],0
#    jmp .L2
#.L3:
#    mov eax,DWORD PTR [rbp-16]
#    mov edx,DWORD PTR [rbp-8]
#    mov rax,QWORD PTR [rdx+rax*8]
#    mov edx,DWORD PTR [rbp-12] 
#    mov eax,DWORD PTR [rax+rdx*4]
#    mov edx,eax
#    mov eax,DWORD PTR [rbp-16]
#    mov ecx,DWORD PTR [rbp-8]
#    mov rax,QWORD PTR [rcx+rax*8]
#    mov rdx,QWORD PTR [rax]
#    mov eax,DWORD PTR [rbp-12]
#    mov eax,DWORD PTR [rdx+rax*4]
#    mov edx,eax
#    mov eax,DWORD PTR [rbp-16]
#    mov ecx,DWORD PTR [rbp-8]
#    mov rax,QWORD PTR [rcx+rax*8]
#    mov rdx,QWORD PTR [rax]
#    mov eax,DWORD PTR [rbp-12]
#    mov eax,DWORD PTR [rdx+rax*4]
#    mov edx,eax
#    mov eax,DWORD PTR [rbp-16]
#    mov ecx,DWORD PTR [rbp-8]
#    mov rax,QWORD PTR [rcx+rax*8]
#    mov rdx,QWORD PTR [rax]
#    mov eax,DWORD PTR [rbp-12]
#    mov eax,DWORD PTR [rdx+rax*4]
#    mov edx,eax


#what even is this?
#this is assembly

#give me a break
"""