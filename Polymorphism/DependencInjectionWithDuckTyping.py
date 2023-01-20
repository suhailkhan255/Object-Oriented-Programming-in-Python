# Dependency injection in passing an object to another object

class Flight:
    def __init__(self, engine):
        self.engine = engine
    def startEngine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print(" starting airBuss engine")

class BoingEngine:
    def start(self):
        print("start BooingEngine")

ae= AirbusEngine()
f = Flight(ae)
f.startEngine()

