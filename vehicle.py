class Vehicle:
    def __init__(self, id, year, make, model, mileage):
        self.id = id
        self.year = int(year)
        self.make = make.title()
        self.model = model.title()
        self.mileage = int(mileage)

    def __str__(self):
        return f"ID:{self.id} {self.year} {self.make} {self.model} - {self.mileage:,} miles"
