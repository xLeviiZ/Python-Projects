def class_average():
    file = open("Students-IQ-Info.txt", "r")
    lines = file.readlines()
    file.close()
    total_iq = 0
    for line in lines:
        parts = line.strip().split(";")
        total_iq += int(parts[2])
    avg = total_iq / len(lines)
    print(f"Class Average IQ: {avg:.2f}")

def show_student_iq():
    name = input("Enter student's name: ")
    file = open("Students-IQ-Info.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        parts = line.strip().split(";")
        if parts[0].lower() == name.lower():
            print(f"{parts[0]}'s IQ: {parts[2]}")
            return
    print("Student not found.")

def show_all_students():
    file = open("Students-IQ-Info.txt", "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        name, age, iq = line.strip().split(";")
        print(f"Name: {name}, Age: {age}, IQ: {iq}")

def add_student():
    name = input("Name: ")
    age = input("Age: ")
    iq = input("IQ: ")

    with open("Students-IQ-Info.txt", "a") as file:
        file.write("\n" + f"{name};{age};{iq}")
    print("Student added successfully.")

def menu():

    while True:
        print("1: Show class average IQ")
        print("2: Show a specific student's IQ")
        print("3: Show all students IQ")
        print("4: Add new student")
        print("5: Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            class_average()
        elif choice == "2":
            show_student_iq()
        elif choice == "3":
            show_all_students()
        elif choice == "4":
            add_student()
        elif choice == "5":
            print("Program stopped.")
            break
        else:
            print("Invalid choice.")

menu()
