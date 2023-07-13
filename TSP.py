import random
import turtle

from math import dist

#tsp attempt two

#idea one: go to nearest
#will not work
pass

#idea two: OSYM algorithm
#find 2 of the shortest paths a city has to any city. There should be 2 of every road. match the same roads side by side to create a chain.
# it did not work
# DEPLOY THE LOOP DETECTION AND CONNECTION ALGORITHM!

prebuiltcities = {"A":(0,0),
                  "B":(50,-85),
                  "C":(101,-171),
                  "D":(-85,-100),
                  "E":(153,-258),
                  "F":(206,-346)}

def genrandomcities(count):
    das_alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    randomcities = {}
    for i in range(count):
        randomcities[das_alphabet[i]] = (random.randrange(-350,350),random.randrange(-350,350))
    return randomcities


#calculate every distance

def CreateDistancesDict(CoordsDict):
    DistsDict = {}
    for start in CoordsDict:
        for end in CoordsDict:
            if start < end:
                temp = dist(CoordsDict[start],CoordsDict[end])
                cities = (start,end)
                DistsDict[cities] = temp
            else:
                pass
    print(DistsDict)
    return DistsDict

def CreateTwoShortest(cities,sorted_distances_list):
    TwoShortest = {}
    for city in cities:
        distsforcity = []
        for dist in sorted_distances_list:
            if city in dist:
                distsforcity.append(dist)
        TwoShortest[city]=(distsforcity[0],distsforcity[1])
    print(f"TwoShortest:    {TwoShortest}")
    return TwoShortest

def StarterFinder(d): #GTP nin yalancısıyım valla
    unique_pairs = set()
    pairs = set()
    for key, value in d.items():
        for pair in value:
            if pair in pairs:
                unique_pairs.discard(pair)
            else:
                pairs.add(pair)
                unique_pairs.add(pair)
    unique_keys = set()
    for key, value in d.items():
        for pair in value:
            if pair in unique_pairs:
                unique_keys.add(key)
    print(f"starting options are:    {unique_keys}\nwe will start with the first one")
    return tuple(unique_keys)

def Visualize(coords):
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    for key in coords:
        turtle .penup()
        turtle.goto(coords[key])
        turtle.dot(10,random.choice(colors))
        turtle.write(key)

def Travel(route,coords):
    for i in range(len(route)-1):
        turtle.penup()
        turtle.goto(coords[route[i]])
        turtle.pendown()
        turtle.goto(coords[route[i+1]])
    turtle.mainloop()

def main(CityCoords):
    #CREATE THE DISTANCES DICT
    DistDict = CreateDistancesDict(CityCoords)

    #SORT THE DISTANCES
    sorted_distances_list = sorted(DistDict.keys(), key=lambda x: DistDict[x])
    print(f"SORTED:     {sorted_distances_list}")

    #FIND THE 2 SHORTEST LINK OF EVERY CITY
    cities = list(CityCoords.keys())
    print(f"CITIES ARE:    {cities}")
    TwoShortest = CreateTwoShortest(cities,sorted_distances_list)

    #FIND THE STARTER
    start = StarterFinder(TwoShortest)[0]
    print(f"starting with {start}")

    #assemble the chain
    route = [start]
    for key in TwoShortest:
        if key == start:
            pass
        elif TwoShortest[key][0] in TwoShortest[route[-1]] or TwoShortest[key][1] in TwoShortest[route[-1]]:
            route.append(key)
    print(f"route is:    {route}")

    #visualize the map
    Visualize(CityCoords)

    #let the salesman travel
    Travel(route,CityCoords)



main(CityCoords= genrandomcities(10))




