
file = open("names.txt","a")

##for name in file:
##    print(name)

names = input("Enter name: ")

file.write("\n"+names)

while names !="zero":
    names = input("Enter name: ")
    file = open("names.txt","a")
    file.write("\n"+names)
    
file.close()

##file.close()
##    
##Israe    

##file.close()

##print(file.readline())
