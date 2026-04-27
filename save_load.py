from vehicle import Vehicle
from db import load_vehicle_db


def load_garage():
    rows = load_vehicle_db()

    loaded_garage = []

    for row in rows:
        vehicle = Vehicle(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
            )
        loaded_garage.append(vehicle)

    return loaded_garage


garage = load_garage()
