import json
from vehicle import Vehicle


def load_garage():
    try:
        with open("garage.json", "r") as file:
            garage_data = json.load(file)

        loaded_garage = []

        for car_data in garage_data:
            vehicle = Vehicle(
                car_data["year"],
                car_data["make"],
                car_data["model"],
                car_data.get("mileage", 0)
            )
            loaded_garage.append(vehicle)

        return loaded_garage

    except FileNotFoundError:
        return []


garage = load_garage()


def save_garage(garage):
    garage_data = []

    for car in garage:
        vehicle_dict = {
            "year": car.year,
            "make": car.make,
            "model": car.model,
            "mileage": car.mileage

        }

        garage_data.append(vehicle_dict)

    with open("garage.json", "w") as file:
        json.dump(garage_data, file, indent=4)
