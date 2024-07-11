# Filename: 151438_q3.py

class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def display_info(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def display_info(self):
        return super().display_info() + f", Number of Seats: {self.number_of_seats}"

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return super().display_info() + f", Cargo Capacity: {self.cargo_capacity} tons"

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return super().display_info() + f", Engine Capacity: {self.engine_capacity} cc"

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.registration_number} added successfully.\n")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.\n")
        else:
            print("List of vehicles in the fleet:")
            for vehicle in self.vehicles:
                print(vehicle.display_info())
            print("")

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print(f"Vehicle found: {vehicle.display_info()}\n")
                return
        print(f"No vehicle found with the registration number {registration_number}.\n")

def main():
    fleet = Fleet()
    
    while True:
        print("Transport Fleet Management System")
        print("1. Add a new vehicle")
        print("2. Display all vehicles")
        print("3. Search for a vehicle by registration number")
        print("4. Exit the program")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            vehicle_type = input("Enter vehicle type (car/truck/motorcycle): ").lower()
            registration_number = input("Enter registration number: ")
            make = input("Enter make: ")
            model = input("Enter model: ")
            if vehicle_type == 'car':
                number_of_seats = input("Enter number of seats: ")
                vehicle = Car(registration_number, make, model, number_of_seats)
            elif vehicle_type == 'truck':
                cargo_capacity = input("Enter cargo capacity (tons): ")
                vehicle = Truck(registration_number, make, model, cargo_capacity)
            elif vehicle_type == 'motorcycle':
                engine_capacity = input("Enter engine capacity (cc): ")
                vehicle = Motorcycle(registration_number, make, model, engine_capacity)
            else:
                print("Invalid vehicle type. Please try again.\n")
                continue
            fleet.add_vehicle(vehicle)
        elif choice == '2':
            fleet.display_vehicles()
        elif choice == '3':
            registration_number = input("Enter registration number: ")
            fleet.search_vehicle(registration_number)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
