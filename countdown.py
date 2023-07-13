import time
def countdown(n):
    if n <= 0:
        print("we are done ")
    else:
        print(n)
        n = n-1
        countdown(n)

countdown(100)
