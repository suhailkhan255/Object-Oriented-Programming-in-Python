class Car:
    def __init__(self, year):
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number
        
        def start(self):
            print("Engine Started")

c= Car(2017)
e =c.Engine(123)
e.start()