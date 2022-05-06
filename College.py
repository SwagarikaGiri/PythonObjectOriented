class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age=age
        self.grade = grade

    def get_grade(self):
        return self.grade



class Course():
    def __init__(self,name,max_students):
        self.name =name
        self.max_students= max_students
        self.students=[]
        self.isActive = False

    def add_student(self,student):
        if(len(self.students)<self.max_students):
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value =0
        for student in self.students:
            value = value + student.get_grade()
        return value/len(self.students)



s1 = Student("A",19,98)
s2 = Student("B",19,95)
s3 = Student("C",19,90)

c1 = Course("Science",4)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
print(c1.get_average_grade())    
