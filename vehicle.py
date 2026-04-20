class Vehicle:
    def __init__(self, year, make, model, mileage):
        self.year = int(year)
        self.make = make.title()
        self.model = model.title()
        self.mileage = int(mileage)
    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.mileage:,} miles"