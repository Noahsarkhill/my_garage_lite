from vehicle import Vehicle


garage = []


def add_vehicle(garage):
    year = int(input("What is the year of your vehicle: "))
    make = input("What is the make of your vehicle: ").title()
    model = input("What is the model of your vehicle: ").title()
    new_vehicle = Vehicle(year, make, model)

    garage.append(new_vehicle)


def view_garage(garage):
    garage_open = True
    while garage_open:
        print("GARAGE MENU")
        if not garage:
            print("Your garage is empty")
        else:
            print("Your cars:")
            for car in garage:
                print(car)
        
        print("1: Add Vehicle: ")
        print("2: Exit Garage: ")
        user_g_choice = input("what would you like to do: ")
        if user_g_choice == "1":
            add_vehicle(garage)
        elif user_g_choice == "2":
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
            print("Good Bye")
            app_running = False
        else:
            print("please select a valid entry: ")
        

main_menu()
    


    


