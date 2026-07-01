
# Student Management System

students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add New Student")
    print("2. Update Marks")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Remove Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # 1. Add New Student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        students[roll] = {
            "name": name,
            "age": age,
            "marks": marks
        }

        print("Student added successfully!")

    # 2. Update Marks
    elif choice == "2":
        roll = input("Enter Roll Number: ")

        if roll in students:
            new_marks = float(input("Enter New Marks: "))
            students[roll]["marks"] = new_marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    # 3. Search Student
    elif choice == "3":
        roll = input("Enter Roll Number: ")

        student = students.get(roll)

        if student:
            print("\nStudent Details:")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
        else:
            print("Student not found!")

    # 4. Display All Students
    elif choice == "4":
        if students:
            print("\nAll Students:")
            for roll, details in students.items():
                print(f"\nRoll No: {roll}")
                print("Name:", details["name"])
                print("Age:", details["age"])
                print("Marks:", details["marks"])
        else:
            print("No students available!")

    # 5. Remove Student
    elif choice == "5":
        roll = input("Enter Roll Number: ")

        if roll in students:
            removed_student = students.pop(roll)
            print("Removed Student:", removed_student)
        else:
            print("Student not found!")

    # 6. Exit
    elif choice == "6":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")