# Student Marks Record System using File Handling
def add_record():
    name = input("Enter Student Name: ")
    subject = input("Enter Subject: ")
    marks = input("Enter Marks: ")
    with open("records.txt", "a") as f:
        f.write(f"{name},{subject},{marks}\n")
    print("Record Added Successfully!")

def view_records():
    try:
        with open("records.txt", "r") as f:
            print("\n--- Student Records ---")
            for line in f:
                name, subject, marks = line.strip().split(",")
                print(f"Name: {name} | Subject: {subject} | Marks: {marks}")
    except FileNotFoundError:
        print("No records found! Please add a record first.")

def search_record():
    search_name = input("Enter student name to search: ")
    found = False
    try:
        with open("records.txt", "r") as f:
            for line in f:
                name, subject, marks = line.strip().split(",")
                if name.lower() == search_name.lower():
                    print(f"Found: Name: {name}, Subject: {subject}, Marks: {marks}")
                    found = True
        if not found:
            print("Record not found!")
    except FileNotFoundError:
        print("No records found!")
# Simple Menu
while True:
    print("\n--- Student Record Menu ---")
    print("1. Add Record")
    print("2. View All Records")
    print("3. Search Record")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        search_record()
    elif choice == "4":
        print("Exiting... Bye!")
        break
    else:
        print("Invalid choice! Please try again.")
