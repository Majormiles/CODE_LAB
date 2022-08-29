

file = open("names.txt","a")
##for x in file:
##    print(x)

names = input("Enter name: ")
file.write("\n"+names)

while names !="0":
    names = input("Enter name: ")
    file = open("names.txt","a")
    file.write("\n"+names)

file.close()


