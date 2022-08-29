import random

##def draw():
##
##    numbers = []
##    for x in range (0,5):
##        if len(numbers)<5:
##            numbers.append((random.randint(1,91)))
##    return numbers

##
##print(draw())

####random.randint
##    
##    numbers = []
##    for i in range(1,91):
##        if (len(number <6)):
##            numbers.append(i)
##        return numbers;
    
    
    

code = input("Enter code: ")

if (code == '*959#'):
    print("1. Monday Special\n2. Draw Results ")

    option = input("Enter choice ")
    
    #CHOOSE FROM THE DROP-DOWN MENU
    if option =='1':
        print("1. Direct-1\n2. Two Sure\n3. Direct-3\n4. Direct-4\n5. Direct-5")
        print()
        print("Select a number from the menu from 1 - 90")

        #ACCEPT INPUT FROM THE USER
        option = input("Enter choice: ")
        
        #SELECT OPTION FROM 1-90
        if ((option =='1')or(option=='2')or(option=='3')):
            Entry = int(input("Enter a number (1-90): "))
            if Entry in range(1, 90):
                print("You've selected ",Entry)

                #ACCEPT AN AMOUNT FROM THE USER
                Amount = float(input("Enter the Amount you wish to Stake(1-200): "))
                print("Your amount is %.2f" %Amount)
            else:
                print("Try again")
             
        else:
            print("Invalid input")
        
    else:
        print("Unknown application")
        print()
    


def draw():

    numbers = []
    for x in range (0,5):
        if len(numbers)<5:
            numbers.append((random.randint(1,91)))
    return numbers

print ("Winning result is: ",draw())


