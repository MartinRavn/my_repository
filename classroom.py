class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    

class Student(Person):
    def __init__(self, first_name, last_name, subject):
        super(Student, self).__init__(first_name, last_name)
        self.subject = subject
    
    def printNameSubject(self):
        full_name = self.get_name()
        print("%s, %s" % (full_name, self.subject))


class Teacher(Person):
    def __init__(self, first_name, last_name, course):
        super(Teacher, self).__init__(first_name, last_name)
        self.subject = course
    
    def printNameSubject(self):
        full_name = self.get_name()
        print("%s, %s" % (full_name, self.course))