'''
Example 15 — Composition vs Inheritance
'''
class Engine:

    def start(self):
        return "Engine started"


class ElectricMotor:

    def start(self):
        return "Electric motor started"


class Vehicle:

    def __init__(self, power_unit):
        self.power_unit = power_unit

    def start(self):
        return self.power_unit.start()


petrol_car = Vehicle(Engine())
electric_car = Vehicle(ElectricMotor())

print(petrol_car.start())
print(electric_car.start())