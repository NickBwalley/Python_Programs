class Student:#Creating a Students class
    #creating a student data-type(user-defined)
    #we can model real-world objects and we can create data-types
    def __init__(self, name, stdNo, gpa, is_on_probation):
        self.name = name
        self.stdNo = stdNo
        self.gpa = gpa
        self.is_on_probation = is_on_probation