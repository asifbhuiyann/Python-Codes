from random import randint
guessnumber = int(input("Enter guess number from 1 to 5 :\n"))
randomnumber = randint(1,5)
if guessnumber == randomnumber :
    print("You have won")
else:
    print("You have lost")
    print("Random Number was:",randomnumber)
