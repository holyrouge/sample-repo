import random

def guessnum ():
    maxsize = input("Please input the range of the unknown number: ")
    unk_num = random.randint(0, maxsize)
    num = -1

    while unk_num != num:
        num = input("Please identify the random number: ")

        if isinstance(num, int) == True:
            if (num > unk_num) and ((num >= (unk_num - 5)) or (num <= (unk_num + 5))):
                print "Your guess is greater than the unknown number and is very close to it."
            elif (num < unk_num) and ((num >= (unk_num - 5)) or (num <= (unk_num + 5))):
                print "Your guess is less than the unknown number and is very close to it."
            elif (num > unk_num):
                print "Your guess is greater than the unknown number."
            elif (num < unk_num):
                print "Your guess is less than the unknown number."
        else: 
            print "Please input an integer."

    print "Your guess is correct. The unknown number is " + str(unk_num) + "."  

    pass

guessnum()