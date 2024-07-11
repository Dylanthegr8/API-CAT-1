# Filename: 151438_q2.py

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # grades should be a dictionary {subject: grade}

    def get_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.\n")

    def display_students(self):
        if not self.students:
            print("No students in the classroom.\n")
        else:
            print("List of students:")
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")
            print("")

    def get_student_average(self, name):
        for student in self.students:
            if student.name == name:
                print(f"Average grade for {name}: {student.get_average_grade()}\n")
                return
        print(f"No student found with the name {name}.\n")

    def get_class_average(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count > 0:
            print(f"Class average for {subject}: {total / count}\n")
        else:
            print(f"No grades found for subject {subject}.\n")

def main():
    classroom = Classroom()
    
    while True:
        print("School Class Management System")
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Get average grade of a student")
        print("4. Get class average for a subject")
        print("5. Exit the program")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter student's name: ")
            grades_input = input("Enter student's grades (e.g., math:90,science:85): ")
            grades = dict(item.split(":") for item in grades_input.split(","))
            grades = {k: int(v) for k, v in grades.items()}
            student = Student(name, grades)
            classroom.add_student(student)
        elif choice == '2':
            classroom.display_students()
        elif choice == '3':
            name = input("Enter the name of the student: ")
            classroom.get_student_average(name)
        elif choice == '4':
            subject = input("Enter the subject: ")
            classroom.get_class_average(subject)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
