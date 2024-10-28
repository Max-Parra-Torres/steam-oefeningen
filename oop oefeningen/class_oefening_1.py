# Create a class with instance attributes

class car:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelS = car(180, 1976)
print(modelS.max_speed, modelS.mileage)
