from save_load import load_garage, save_garage
from garage_manager import view_garage, add_vehicle, search_vehicles
from utils import get_int


def main_menu():
    garage = load_garage()
    app_running = True

    while app_running:
        print("MAIN MENU")
        print("1: Add vehicle")
        print("2: Search vehicle")
        print("3: Show Garage")
        print("4: EXIT")

        user_choice = get_int("What would you like to do: ", 1, 5)
        if user_choice == 1:
            add_vehicle(garage)
        elif user_choice == 2:
            search_vehicles(garage)
        elif user_choice == 3:
            view_garage(garage)
        elif user_choice == 4:
            save_garage(garage)
            print("Good Bye")
            app_running = False


main_menu()
