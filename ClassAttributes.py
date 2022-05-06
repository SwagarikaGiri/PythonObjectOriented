class Person:
    number_of_people =0
    def __init__(self,name):
        self.name = name
        Person.number_of_people+=1


#act on class itself and it has no control on instance
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people


p1 = Person("tim")
print(p1.number_of_people)
p2 = Person("jilly")
print(p2.number_of_people_())