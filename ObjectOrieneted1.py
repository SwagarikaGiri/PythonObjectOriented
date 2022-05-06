from html.entities import name2codepoint



class Dog:
    def __init__(self,name):
        self.name=name
        print(name)
    
    def add_one(self,x):
        return x+1

    def bark(self):
        print("bark")

d =Dog("Tim")
print(type(d))