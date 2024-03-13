import random
min_value=1
max_value=6
start="yes"
while start=="yes":
    print("Let's start the rolling of dice")
    print("the value is:")
    dice1=(random.randint(min_value,max_value))
    dice2=(random.randint(min_value,max_value))
    print(dice1)
    print(dice2)
    if(dice1==dice2):
        print("Both dice are showing same number")
    else:
         print("Both dice are showing different number")
    start=input("Do you want to roll the dice again?")     