class Student:
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major


    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getMajor(self):
        return self.major

    #returns tuple of Student
    def getStudent(self):
        return (self.getFirstName(), self.getLastName(), self.getMajor())
