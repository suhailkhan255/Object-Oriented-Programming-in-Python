"""In python interfaces is just a step above abstraction
an interface is class with all the method as abstract """

"""
 1.A method which is has declaration but no definition is called abstract method
 2.A Class which has abstract method is call abstract class
 3.we can not create the objects of abstract class
 4.All the child classes should implement abstract method"""

# method Overriding is used to achieve run time polymorphism
from abc import abstractmethod, ABC


class BMW(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # All the child classes should implement this abstract method
    @abstractmethod
    def start(self):
        pass

    # All the child classes should implement this abstract method
    @abstractmethod
    def stop(self):
        pass

    # All the child classes should implement this abstract method
    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):

    def __init__(self, cruiceControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruiceControlEnabled = cruiceControlEnabled

    def stop(self):
        print("stoping the threeseries car")

    def drive(self):
        print("three series is being driven")

    def start(self):
        print("three series is being driven")



class FiveSeries(BMW):
    def __init__(self, cruiceControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruiceControlEnabled = cruiceControlEnabled

    def drive(self):
        print("three series is being driven")

    def stop(self):
        print("stoping the threeseries car")

    def stop(self):
        print("three series is being driven")


threeSeries = ThreeSeries(True, "bmw", "328i", 2018)
print(threeSeries.cruiceControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.stop()
threeSeries.start()
