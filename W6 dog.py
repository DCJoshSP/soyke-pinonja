#W6 Task 1
#class definition for Dog
class Dog():
    
    def __init__(self, name, colour):
        self.p_name = name
        self.p_colour = colour
        
    def bark(self, barkTimes):
        for n in range (barkTimes):
            print("Woof!")
            
##    def setColour(self,myColour):
##        self.p_colour = myColour
##        
##    def getColour(self):
##        return self.p_colour
##        
##    def getName(self):
##        return self.p_name
##    
##    def printDogDetails(self):
##        print (self.p_name, self.p_colour)
    

        
myDog1 = Dog("Fido", "Black")
myDog2 = Dog ("Bonnie","Golden")
myDog3 = Dog ("Mutt", "Unknown")
myDog4 = Dog ("Jeff", "Unknown")
myDog3.bark(3)
print("\n")
if myDog3.p_colour == "Unknown":
    print("Please enter colour for", myDog3.p_name)
    newColour = input()
    myDog3.setColour (newColour)
print(myDog3.getName(), "is now set to", myDog3.p_name)

# these are alternative statements  for getting, setting and printing
print("\n ... and extra print statements")
dog2Name = myDog2.getName()
dog2Colour = myDog2.getColour()
print (dog2Name, dog2Colour)

myDog4.printDogDetails()



                  
