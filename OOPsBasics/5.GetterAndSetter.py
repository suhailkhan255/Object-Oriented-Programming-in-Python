class Programmer:
    def setName(self,n):
        self.name=n

    def getName(self):
        return self.name

obj= Programmer()

obj.setName("suhail")
print(obj.getName())