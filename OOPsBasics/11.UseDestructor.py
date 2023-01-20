class Car:
    def __init__(self):
        self.year = 2021
        self.model = "xls"

    def __del__(self):
        print("inside the distructor")

    def display(self):
        print(self.year)
        print(self.model)
        
p1 = Car()
p1.display()
p1 =None

