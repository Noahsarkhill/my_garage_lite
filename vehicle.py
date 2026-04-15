class Vehicle:
    def __init__(self, year, make, model):
        self.year = int(year)
        self.make = make
        self.model = model
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"