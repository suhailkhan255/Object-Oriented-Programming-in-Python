class Student:
    major ="CSE"

    def __init__(self, rollnumber, name):
        self.rollnumber = rollnumber
        self.name = name

s1= Student(55,"Danish")
print(s1.major)
print(Student.major)