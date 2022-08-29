class Human():
    #Initialising a class
    
    def __init__(self, p_name,p_height,p_gender):

        self.p_name= name
        self.p_gender = gender
        self.p_height = height
        p_noun= pnoun
        
    #Defining a method

    def talk(self):
        if self.p_gender=="M":
            p_noun = "He"
        elif self.p_gender=="F":
            p_noun = "She"
        return "{} said mama ""{}\n is a male ""{}\nEven though he is a ""{}\n".format(self.p_gender,self.p_noun,self.gender,self.p_height)
      
first_human = Human("Adam", "M", "6ft")
Second_human = Human("Moses","M", "9ft")
Third_human = Human("Bliss","M","11ft")
Forth_human = Human("Amina","F","7ft")


print(first_human.talk())
print()
print(Second_human.talk())
print()
print(Third_human.talk())
print()
print(Forth_human.talk())


