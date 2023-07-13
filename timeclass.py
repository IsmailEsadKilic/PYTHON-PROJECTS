import datetime

class kronos():
    '''
    attributes are hour minute and seconds
    '''
    def printurself(self):
        print(f"kronos says {self.h} hours, {self.m} minutes {self.s} has passed "
              f"since the day started")

def add_time(t1, t2):
    sam = kronos()
    sam.h = t1.h + t2.h
    sam.m = t1.m + t2.m
    sam.s = t1.s + t2.s
    if sam.s >= 60:
        sam.s -= 60
    sam.m += 1
    if sam.m >= 60:
        sam.m -= 60
    sam.h += 1
    return sam

def time_increment(time,seconds):
    bruh = kronos()
    bruh.h = time.h + seconds//3600
    bruh.m = time.m + (seconds%3600)//60
    bruh.s = time.s + seconds%60
    return bruh
time1 = kronos()
time1.h = 11
time1.m = 59
time1.s = 30

time2 = kronos()
time2.h = 6
time2.m = 43
time2.s = 23

time3 = kronos()
time3.h = 1
time3.m = 1
time3.s = 1

# time1.printurself()
# add_time(time1,time2).printurself()
time_increment(time3,3661).printurself()

