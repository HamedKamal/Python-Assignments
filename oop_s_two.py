
class Animal:
    def __init__(self,numberOfLegs,age,typee):
        self.numberOfLegs=numberOfLegs
        self.age=age
        self.type=typee
    def eat(self):
        print(f"Animal is eating")
class Dog(Animal):

    def eat(self):
        print(f"{self.name} is eating")

    def eat(self,food):
        print(f"{self.name} eating {food}")
    def __init__(self,name,numberOfLegs,age,typee) :
        self.name=name
        Animal.__init__(self,numberOfLegs,age,typee)
        
class DogChild(Dog):
    def __init__(self, numberOfMonths,name,numberOfLegs,age,typee):
        self.numberOfmonths=numberOfMonths
        self.name=name
        Animal.__init__(self,numberOfLegs,age,typee)
        print(f"child dog  {self.name}")

class Cat(Animal):
    def __init__(self,name,numberOfLegs,age,typee) :
        self.name=name
        print(f"cat name {self.name}")
        Animal.__init__(self,numberOfLegs,age,typee)
    
mydog=Dog(name='simba',numberOfLegs=8,age=6,typee='golden')
mydog.eat('fish')
mydog.eat()

mychilddog=DogChild(name='simba son',numberOfLegs=4,age=6,typee='golden',numberOfMonths=8)
mydog=Cat(name='cat simba',numberOfLegs=8,age=6,typee='sherazi')
