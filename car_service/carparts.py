ElectricalsCar = "Electrical Car"
SportsCar = "Sports Car"
twoWheelsCar = "2 Wheel Car"

class Engine:
    def __init__(self, capacity, num_cylinders):
        self.capacity = capacity
        self.num_cylinders = num_cylinders

class Transmission:
    def __init__(self, type):
        self.type = type

class FuelType:
    def __init__(self, type):
        self.type = type

class Color:
    def __init__(self, exterior, interior):
        self.exterior = exterior
        self.interior = interior

class CarBodyStyle:
    def __init__(self, style, size):
        self.style = style
        self.size = size

class CarPart:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        

class Chassis(CarPart):
    def __init__(self, name):
        super().__init__(name, "Chassis")

class BrakingSystem(CarPart):
    def __init__(self, name):
        super().__init__(name, "Braking System")

class Electrical(CarPart):
    def __init__(self, name):
        super().__init__(name, ElectricalsCar)

class Battery(CarPart):
    def __init__(self, name):
        super().__init__(name, ElectricalsCar)
    
class Alternator(CarPart):
    def __init__(self, name):
        super().__init__(name, ElectricalsCar)

class AlternatorPulley(CarPart):
    def __init__(self, name):
        super().__init__(name, ElectricalsCar)

class SerpentineBelt(CarPart):
    def __init__(self, name):
        super().__init__(name, twoWheelsCar)

class CoolingSystem(CarPart):
    def __init__(self, name):
        super().__init__(name, twoWheelsCar)

class Radiator(CarPart):
    def __init__(self, name):
        super().__init__(name, twoWheelsCar)

class LubricationSystem(CarPart):
    def __init__(self, name):
        super().__init__(name, twoWheelsCar)

class IgnitionSystem(CarPart):
    def __init__(self, name):
        super().__init__(name, "Ignition System")

class PowerTrain(CarPart):
    def __init__(self, name):
        super().__init__(name, "Power Train")

class Clutch(CarPart):
    def __init__(self, name):
        super().__init__(name)

class PropellerShaft(CarPart):
    def __init__(self, name):
        super().__init__(name)

class Differential(CarPart):
    def __init__(self, name):
        super().__init__(name)

class Axles(CarPart):
    def __init__(self, name):
        super().__init__(name, SportsCar)

class GearShift(CarPart):
    def __init__(self, name):
        super().__init__(name, SportsCar)

class TimingBelt(CarPart):
    def __init__(self, name):
        super().__init__(name, SportsCar)

class SuspensionSystem(CarPart):
    def __init__(self):
        super().__init__("Suspension System")

class ShockAbsorber(CarPart):
    def __init__(self):
        super().__init__("Shock Absorber")

class ExhaustSystem(CarPart):
    def __init__(self):
        super().__init__("Exhaust System")

class Sensor(CarPart):
    def __init__(self):
        super().__init__("O2 Sensor")

class CatalyticConverter(CarPart):
    def __init__(self):
        super().__init__("Catalytic Converter")

class Resonator(CarPart):
    def __init__(self):
        super().__init__("Resonator")

class Mufflers(CarPart):
    def __init__(self):
        super().__init__("Mufflers")

class ExhaustManifold(CarPart):
    def __init__(self):
        super().__init__("Exhaust Manifold")

class ElectronicControlUnit(CarPart):
    def __init__(self):
        super().__init__("Electronic")