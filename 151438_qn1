# Filename: 151438_q1.py

def add_patient(patients):
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    patients.append({'name': name, 'age': age, 'illness': illness})
    print(f"Patient {name} added successfully.\n")

def display_patients(patients):
    if not patients:
        print("No patients in the system.\n")
    else:
        print("List of patients:")
        for idx, patient in enumerate(patients, start=1):
            print(f"{idx}. Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
        print("")

def search_patient(patients):
    name = input("Enter the name of the patient to search for: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Patient found: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}\n")
            return
    print(f"No patient found with the name {name}.\n")

def remove_patient(patients):
    name = input("Enter the name of the patient to remove: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            patients.remove(patient)
            print(f"Patient {name} removed successfully.\n")
            return
    print(f"No patient found with the name {name}.\n")

def main():
    patients = []
    while True:
        print("Hospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit the program")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            remove_patient(patients)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
