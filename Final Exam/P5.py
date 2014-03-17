class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

class Singer(Lecturer):
    def sing(self, stuff):
        return stuff + ' Tra la la'
    def lecture(self, stuff):
        return self.sing(Lecturer.lecture(self, stuff))

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return 'It is obvious that ' + self.lecture(stuff)


e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
se = Singer('eric')
ae = ArrogantProfessor('eric')

print ae.lecture('the sky is blue')