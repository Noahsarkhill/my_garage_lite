import json
from vehicle import Vehicle



def save_garage(garage):
    garage_data = []

    for car in garage:
        vehicle_dict = {
            "year": car.year,
            "make": car.make,
            "model": car.model
        }

        garage_data.append(vehicle_dict)
    
    with open("garage.json", "w") as file:
        json.dump(garage_data, file, indent=4)

def load_garage():
    try:
        with open("garage.json", "r") as file:
            garage_data = json.load(file)

        loaded_garage = []

        for car_data in garage_data:
            vehicle = Vehicle(
                car_data["year"],
                car_data["make"],
                car_data["model"]
            )
            loaded_garage.append(vehicle)

        return loaded_garage
    
    except FileNotFoundError:
        return []

garage = load_garage()



def add_vehicle(garage):
    while True:
        try:
            year = int(input("What is the Year of your vehicle: "))
            

            if year < 1950 or year >= 2100:
                print("Please enter a valid year")
                continue

            break

        except ValueError:
            print("Please enter a valid vear")

    make = input("What is the Make of your vehicle: ")
    model = input("What is the Model of your vehicle: ")
    new_vehicle = Vehicle(year, make, model)

    garage.append(new_vehicle)


def delete_vehicle(garage):
    if not garage:
        print("Your Garage is empty")
        return
    while True:
        try:
            user_delete = int(input("Which car would you like to delete: ")) - 1

            if user_delete < 0 or user_delete >= len(garage):
                print("Invalid Selection")
                continue
    
            deleted_car = garage.pop(user_delete)
            print(f"You Deleted {deleted_car}")
            break

        except ValueError:
            print("Please enter a number")

    


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
        print("3: Exit Garage")
        user_g_choice = input("what would you like to do: ")
        if user_g_choice == "1":
            add_vehicle(garage)
        elif user_g_choice == "2":
            delete_vehicle(garage)
        elif user_g_choice == "3":
            garage_open = False





def main_menu():
    app_running = True

    while app_running:
        print("MAIN MENU")
        print("1: Add vehicle")
        print("2: Show Garage")
        print("3: EXIT")

    

        user_choice = input("What would you like to do: ")
        if user_choice == "1":
            add_vehicle(garage)
        elif user_choice == "2":
            view_garage(garage)
        elif user_choice == "3":
            save_garage(garage)
            print("Good Bye")
            app_running = False
        else:
            print("please select a valid entry: ")
        

main_menu()
    


    


