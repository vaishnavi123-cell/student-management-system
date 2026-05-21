import json

# File name
FILE_NAME = "students.json"


# Default Student Data
students = [

    {
        "name": "Rahul",
        "age": 20,
        "marks": 85,
        "subject": "Python"
    },

    {
        "name": "Priya",
        "age": 19,
        "marks": 90,
        "subject": "Java"
    },

    {
        "name": "Amit",
        "age": 21,
        "marks": 78,
        "subject": "C++"
    },

    {
        "name": "Sneha",
        "age": 20,
        "marks": 88,
        "subject": "Data Science"
    },

    {
        "name": "Vaishnavi",
        "age": 22,
        "marks": 95,
        "subject": "Cyber Security"
    }

]

# Save default data to JSON file
with open(FILE_NAME, "w") as file:
    json.dump(students, file, indent=4)


# ---------------- ADD STUDENT ----------------
def add_student():

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    subject = input("Enter Subject: ")

    student = {
        "name": name,
        "age": age,
        "marks": marks,
        "subject": subject
    }

    students.append(student)

    save_data()

    print("Student Added Successfully!")


# ---------------- VIEW STUDENTS ----------------
def view_students():

    if len(students) == 0:
        print("No student records found")
        return

    print("\n----- Student Records -----")

    for i, s in enumerate(students, start=1):

        print(f"\nStudent {i}")
        print("-------------------")
        print("Name :", s["name"])
        print("Age :", s["age"])
        print("Marks :", s["marks"])
        print("Subject :", s["subject"])


# ---------------- DELETE STUDENT ----------------
def delete_student():

    name = input("Enter student name to delete: ")

    for s in students:

        if s["name"].lower() == name.lower():

            students.remove(s)

            save_data()

            print("Student Deleted Successfully!")
            return

    print("Student Not Found")


# ---------------- EDIT STUDENT ----------------
def edit_student():

    name = input("Enter student name to edit: ")

    for s in students:

        if s["name"].lower() == name.lower():

            print("Enter New Details")

            s["age"] = input("New Age: ")
            s["marks"] = input("New Marks: ")
            s["subject"] = input("New Subject: ")

            save_data()

            print("Student Updated Successfully!")
            return

    print("Student Not Found")


# ---------------- SAVE DATA ----------------
def save_data():

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ---------------- MAIN MENU ----------------
while True:

    print("\n====== Student Management System ======")

    print("1. Add Student")
    print("2. View Students")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice:1 ")

    # Add Student
    if choice == "1":
        add_student()

    # View Students
    elif choice == "2":
        view_students()

    # Edit Student
    elif choice == "3":
        edit_student()

    # Delete Student
    elif choice == "4":
        delete_student()

    # Exit
    elif choice == "5":

        print("Program Closed")
        break

    else:
        print("Invalid Choice")