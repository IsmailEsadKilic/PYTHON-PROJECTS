aga = ("wha", "aga")
with open("textimsi.txt","r") as file:
    line = file.read()

print(line)

with open("textimsi.txt","r+") as file:

    #file.write(aga[0])
    pass

with open("textimsi.txt","a") as file:

    #file.write("\nbaris,200401020,90,MEG\n")
    pass

with open("textimsi.txt","r") as file:

    lines = file.readlines()
    print(lines)

with open("textimsi.txt","r") as file:

    for line in file:
        row = line.rstrip().split(',')
        print(f"{row[0]} has {row[2]}")

