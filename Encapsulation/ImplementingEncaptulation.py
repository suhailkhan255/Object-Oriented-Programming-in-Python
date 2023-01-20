class Student:

    def setId(self, id):
        self.id = id

    def getid(self):
        return self.id

s=Student()

s.setId(100)
print(s.getid())