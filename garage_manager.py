from vehicle import Vehicle
from utils import get_int, get_valid_text
from db import save_vehicle_db, update_vehicle_db, delete_vehicle_db


# constant variables for the vehicle years range
START_YEAR = 1950
END_YEAR = 2126


def view_garage(garage):
    garage_open = True
    while garage_open:
        print("GARAGE MENU")
        if not garage:
            print("Your Garage is empty")
        else:
            print("Your cars:")
            for index, car in enumerate(garage):
                print(index + 1, car)

        print("1: Add Vehicle")
        print("2: Delete Vehicle")
        print("3: Edit Vehicle")
        print("4: Exit Garage")
        user_g_choice = get_int("What would  you like to do: ", 1, 5)
        if user_g_choice == 1:
            add_vehicle(garage)
        elif user_g_choice == 2:
            delete_vehicle(garage)
        elif user_g_choice == 3:
            edit_vehicle(garage)
        elif user_g_choice == 4:
            garage_open = False


# Adding a user's vehicle to the garage
def add_vehicle(garage):
    year = get_int("What is the year of your vehicle: ", START_YEAR, END_YEAR)

    make = get_valid_text("What is the Make of your vehicle: ")

    model = get_valid_text("What is the Model of your vehicle: ")

    mileage = get_int("What is your vehicles mileage: ", 0)

    new_vehicle = Vehicle(None, year, make, model, mileage)

    new_id = save_vehicle_db(new_vehicle.year, new_vehicle.make,
                             new_vehicle.model, new_vehicle.mileage)

    new_vehicle.id = new_id
    garage.append(new_vehicle)

    print(f"{year} {make} {model} {mileage} saved!")


# Editing a vehicle function of the user's choice
def edit_vehicle(garage):
    fields = ["year", "make", "model", "mileage"]
    if not garage:
        print("Your Garage is empty")
        return

    print("Your Cars:")
    for index, car in enumerate(garage):
        print(index + 1, car)
    # Getting the user's input on what vehicle they want to edit
    user_edit = get_int("What vehicle would you like to edit: ",
                        1, len(garage) + 1) - 1

    selected_car = garage[user_edit]

    for index, field in enumerate(fields):
        print(index + 1, field)
    # Getting the user's input of which field they want to edit
    edit_choice = get_int("What field woud you like to edit: ",
                          1, len(fields) + 1) - 1

    if edit_choice == 0:
        new_year = get_int("What is the year of your car: ",
                           START_YEAR, END_YEAR)

        selected_car.year = new_year

        print(f"{selected_car.year} updated!")

    elif edit_choice == 1:
        new_make = get_valid_text("What is the make of your car: ")

        selected_car.make = new_make

        print(f"{selected_car.make} updated!")

    elif edit_choice == 2:
        new_model = get_valid_text("What is the model of your car: ")

        selected_car.model = new_model

        print(f"{selected_car.model} updated!")

    elif edit_choice == 3:

        new_mileage = get_int("What is the mileage of your car: ", 0)

        selected_car.mileage = new_mileage

        print(f"{selected_car.mileage} updated!")

    update_vehicle_db(
        selected_car.id,
        selected_car.year,
        selected_car.make,
        selected_car.model,
        selected_car.mileage
    )


def search_vehicles(garage):
    if not garage:
        print("Your Garage is empty")
        return

    user_search = get_valid_text("What vehicle would you like to search: ")
    search_term = user_search.lower().strip()

    found = False

    for car in garage:

        if search_term in car.make.lower() or search_term in car.model.lower():
            if not found:
                print("Search Results:")

            found = True
            print(car)

    if not found:
        print("No vehicles found")


# Deleting a user's vehicle from the garage
def delete_vehicle(garage):
    if not garage:
        print("Your Garage is empty")
        return

    print("Your Cars:")

    for index, car in enumerate(garage):
        print(index + 1, car)

    user_delete = get_int("Which car would you like to delete: ",
                          1, len(garage) + 1) - 1


    selected_car = garage[user_delete]

    delete_vehicle_db(selected_car.id)

    deleted_car = garage.pop(user_delete)

    print(f"You Deleted {deleted_car}")
