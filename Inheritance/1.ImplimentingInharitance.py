class BMW:

    def __init__(self, make, model, year ):
        self.make =make
        self.model =model
        self.year = year

class ThreeSeries(BMW):

    def __init__(self, cruiceControlEnabled, make,model, year ):
        BMW.__init__(self,make,model,year)
        self.cruiceControlEnabled =cruiceControlEnabled

class FiveSeries(BMW):
    def __init__(self, cruiceControlEnabled, make,model, year ):
        BMW.__init__(self,make,model,year)
        self.cruiceControlEnabled =cruiceControlEnabled


threeSeries= ThreeSeries(True, "bmw", "328i", 2018)
print(threeSeries.cruiceControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)