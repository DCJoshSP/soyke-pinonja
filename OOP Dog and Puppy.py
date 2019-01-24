class Dog():
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    #end procedure
    def new(myName, myColour):
        self.name = myName
        self.colour = myColour
    #end procedure
    def bark(barktimes):
        for n in range(1, barktimes):
            print("Woof")
        #next n
    #end procedure
    def setcolour(self, newcolour):
        self.colour = newcolour
    #end procedure
    def getcolour(self):
        return self.colour
    #end procedure
    def getname(self):
        return self.name
    #end procedure  
#end class

myDog3 = Dog("Mutt", "Unknown")
myDog4 = Dog("Jeff", "Unknown")

result = myDog3.getcolour()
if result == "Unknown":
    colour = input("Please enter a new colour")
    myDog3.setcolour(colour)
print(myDog3.getname())
print(myDog3.getcolour())

class Puppy(Dog):
    shoeschewed = 0
    def chewShoe(self,numshoes):
        self.shoeschewed += numshoes
    #end procedure
    def getShoesChewed(self):
        return self.shoeschewed
    #end procedure
#end class



myPuppy = Puppy("Sam", "red")
name = myPuppy.getname()
shoes_chewed = myPuppy.getShoesChewed()
print(name)
print(shoes_chewed)
