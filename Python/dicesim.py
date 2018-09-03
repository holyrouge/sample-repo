import random

def dicesim ():
    while True:
        maxsize = input("Please specify the max size of the dice: ")
        print random.randint(1, maxsize)
        pass
    pass

dicesim()