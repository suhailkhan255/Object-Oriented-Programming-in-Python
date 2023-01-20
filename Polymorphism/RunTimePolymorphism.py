# method Overriding is used to achieve run time polymorphism

class BMW:

    def __init__(self, make, model, year ):
        self.make =make
        self.model =model
        self.year = year

    def start(self):
        print("starting the car")

    def stop(self):
        print("stoping the car")


class ThreeSeries(BMW):

    def __init__(self, cruiceControlEnabled, make,model, year ):
        BMW.__init__(self,make,model,year)
        self.cruiceControlEnabled =cruiceControlEnabled

    def stop(self):
        print("stoping the threeseries car")

class FiveSeries(BMW):
    def __init__(self, cruiceControlEnabled, make,model, year ):
        BMW.__init__(self,make,model,year)
        self.cruiceControlEnabled =cruiceControlEnabled


threeSeries= ThreeSeries(True, "bmw", "328i", 2018)
print(threeSeries.cruiceControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.stop()
threeSeries.start()
