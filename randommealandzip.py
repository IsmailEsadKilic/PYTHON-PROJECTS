import random
yemekler = ("crummble", "noodle", "kurabiye", "çorba", "hamburger")
aşçıagalar = ("bilge aga", "serap aga", "arda aga", "sıddık aga", "esad aga")
içecekler = ("kola", "füsti", "su", "hoşaf", "eyran")

aga = random.choice(aşçıagalar)
yem = random.choice(yemekler)
iç = random.choice(içecekler)


print(f"bugün yemekte {aga} nın yaptığı {yem} yanında {iç} var")

zipilesi = zip(yemekler,aşçıagalar)
print(zipilesi)
print(type(zipilesi))

for item in zipilesi:
    print(item)

testdict = {}
testdict[("kın", 10)] = "kaan"

print(testdict["kın", 10])


