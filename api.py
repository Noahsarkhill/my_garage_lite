from pydantic import BaseModel
from fastapi import FastAPI
from db import load_vehicle_db, save_vehicle_db, delete_vehicle_db, update_vehicle_db

app = FastAPI()

@app.get("/vehicles")
def get_vehicle():
    rows = load_vehicle_db()

    print("ROWS FROM DB", rows)

    vehicles = []

    for row in rows:
        vehicle = {
            "id": row[0],
            "year": row[1],
            "make": row[2],
            "model": row[3],
            "mileage": row[4]
        }

        vehicles.append(vehicle)

    return vehicles

class VehicleCreate(BaseModel):
    year: int
    make: str
    model: str
    mileage: int

@app.post("/vehicles")
def create_vehicle(vehicle: VehicleCreate):
    year = vehicle.year
    make = vehicle.make.title()
    model = vehicle.model.title()
    mileage = vehicle.mileage

    new_id = save_vehicle_db(
        year,
        make,
        model,
        mileage
    )

    if not new_id:
        return {"message": "Vehicle was not added."}
    
    return {
        "message": "Vehicle added successfully",
        "vehicle": {
            "id": new_id,
            "year": year,
            "make": make,
            "model": model,
            "mileage": mileage
        }
    }

@app.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int):

    success = delete_vehicle_db(vehicle_id)

    if not success:
        return {"message": "Vehicle was not deleted"}
    
    return {"message": "Vehicle deleted successfully"}


@app.put("/vehicles/{vehicle_id}")
def edit_vehicle(vehicle_id: int, vehicle: VehicleCreate):
    year = vehicle.year
    make = vehicle.make.title()
    model = vehicle.model.title()
    mileage = vehicle.mileage

    success = update_vehicle_db(
        vehicle_id,
        year,
        make,
        model,
        mileage
        )

    if not success:
        return {"message": "Vehicle was not updated"}
    
    return {"message": "Vehicle updated successfully",
            "vehicle": {
                "id": vehicle_id,
                "year": year,
                "make": make,
                "model": model,
                "mileage": mileage
            }
            }