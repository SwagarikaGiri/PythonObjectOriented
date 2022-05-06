
class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
         print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def speak(self):
        return " Meow"

class Dog(Pet):
    def speak(self):
        return " bark"


p = Pet("Tim",19)
p.show()
c = Cat("Jill",25)
c.show()


    




