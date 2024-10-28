# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

# Given:
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Create a Bus object that will inherit all of the variables and
# methods of the parent Vehicle class and display it.

class Bus(Vehicle):
    pass

school_bus = Bus('Volkswagen polo', 340, 295692)
print(f'{school_bus.name} is met een snelheid van {school_bus.max_speed} door een woonwijk aan het racen.')
