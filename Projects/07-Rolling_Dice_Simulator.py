import random

print("Welcome to rolling dice simulator")
choice=input("Roll Dice? (Y/N) : ")

while(choice=='Y' or choice =='y'):
    num = random.randint(1,6)
    print("-------")
    print("|  {}  |".format(num))
    print("-------")
    
    choice = input(" Do you want to continue? (Y/N) :")
