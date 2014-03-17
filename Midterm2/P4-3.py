class Subject(object):
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)

    def allStudents(self):
        return sorted(self.students)

    def __str__(self):
        return 'Subject with ' + str(len(self.students)) + ' students.'

mySubject = Subject()
p1 = 'Betty Rubble'
p2 = 'Dino'
p3 = 'Fred Flintstone'
p4 = 'Wilma Flintstone'
p5 = 'Barney Rubble'
mySubject.addStudent(p1)
mySubject.addStudent(p2)
mySubject.addStudent(p3)
mySubject.addStudent(p4)
mySubject.addStudent(p5)
for s in mySubject.allStudents():
    print s
