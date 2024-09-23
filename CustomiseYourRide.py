print("Select you ride = ")
print("1. Bike")
print("2. Car")
#take input of number 1 or 2
#select your ride
choice = int(input("Enter you choice = "))
#user entering option 1
if( choice == 1 ): 
    print("What type of bike?")
    print("1. Scooty\n")
    print("2. Scooter\n")

#condition for selecting the type of bike
    choice2=int(input("Enter you choice2 = "))
    if choice2==1:
        print("You have selected scooty.")
    else:
        print("You have selected scooter.")
    #user entering option2 
elif(choice==2): 
    print("What tyoe of car?")
    print("1. Sedan")
    print("2. SUV")
    choice3=int(input("Enter your choice3 = "))
    if choice3==1: 
        print("You have selected Sedan.")
    else:
        print("You have selected SUV")

else:
    print("Wrong choice please try again!")