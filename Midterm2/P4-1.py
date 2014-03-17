class Person(object):
    def __init__(self, name):
        self.name = name
    def __lt__(self, other):
        return self.name < other.name
    def __str__(self):
        return self.name
    def getName(self):
        return self.name

class edXPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = edXPerson.nextIdNum
        edXPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum
    def isStudent(self):
        return isinstance(self, Student)

class Student(edXPerson):
    pass

class UniversityStudent(Student):
    pass

class SelfLearner(Student):
    def __init__(self, name):
        Student.__init__(self, name)
        self.idNum = 0

p1 = edXPerson('Fred Flintstone')
p2 = UniversityStudent('Wilma Flintstone')
p3 = Student('Betty Rubble')
p4 = SelfLearner('Barney Rubble')
p5 = SelfLearner('Dino')
p = Person('Eric Grimson')

#print p2 < p3
#print p2.getIdNum() < p3.getIdNum()
#print p2.name < p3.name
print p4 < p3
print p4 < p5
print p1.isStudent()
print p3.isStudent()
print p5.isStudent()
print p.isStudent()