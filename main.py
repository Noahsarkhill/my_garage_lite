import json
from vehicle import Vehicle


# constant variables for the vehicle years range
START_YEAR = 1950
END_YEAR = 2126

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

# Helper function for text input validation
def get_valid_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field cannot be empty")



# Helper function for number input validation
def get_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
        
            if min_value is not None and value < min_value:
                print("Value is too low")
                continue
            if max_value is not None and value >= max_value:
                print("Value is too high")
                continue

            return value
        
        except ValueError:
            print("Not a valid entry")

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
    user_edit = get_int("What vehicle would you like to edit: ", 1, len(garage) + 1) - 1

    selected_car = garage[user_edit]
    

    for index, field in enumerate(fields):
        print(index + 1, field)
    # Getting the user's input of which field they want to edit
    edit_choice = get_int("What field woud you like to edit: ", 1, len(fields) + 1) - 1
        

    if edit_choice == 0:
        new_year = get_int("What is the year of your car: ", START_YEAR, END_YEAR)
        
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

    save_garage(garage)


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


# Adding a user's vehicle to the garage
def add_vehicle(garage):
    year = get_int("What is the year of your vehicle: ", START_YEAR, END_YEAR)

    make = get_valid_text("What is the Make of your vehicle: ")

    model = get_valid_text("What is the Model of your vehicle: ")

    mileage = get_int("What is your vehicles mileage", 0)

    new_vehicle = Vehicle(year, make, model, mileage)

    garage.append(new_vehicle)
    save_garage(garage)
    print(f"{year} {make} {model} saved!")

# Deleting a user's vehicle from the garage
def delete_vehicle(garage):
    if not garage:
        print("Your Garage is empty")
        return
    
    print("Your Cars:")
        
    for index, car in enumerate(garage):
        print(index + 1, car)

    user_delete = get_int("Which car would you like to delete: ", 1, len(garage) + 1) - 1
    
    
    deleted_car = garage.pop(user_delete)
    print(f"You Deleted {deleted_car}")
            

    save_garage(garage)
    


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
        print("4: Search vehicle")
        print("5: Exit Garage")
        user_g_choice = get_int("What would  you like to do: ", 1, 6)
        if user_g_choice == 1:
            add_vehicle(garage)
        elif user_g_choice == 2:
            delete_vehicle(garage)
        elif user_g_choice == 3:
            edit_vehicle(garage)
        elif user_g_choice == 4:
            search_vehicles(garage)
        elif user_g_choice == 5:
            garage_open = False





def main_menu():
    app_running = True

    while app_running:
        print("MAIN MENU")
        print("1: Add vehicle")
        print("2: Show Garage")
        print("3: EXIT")

    

        user_choice = get_int("What would you like to do: ", 1, 4)
        if user_choice == 1:
            add_vehicle(garage)
        elif user_choice == 2:
            view_garage(garage)
        elif user_choice == 3:
            save_garage(garage)
            print("Good Bye")
            app_running = False
        

main_menu()
    


    


