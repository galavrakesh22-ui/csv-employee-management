import csv
import json

CSV_FILE = "employees.csv"
JSON_FILE = "employees.json"


# ---------- LOAD EMPLOYEES ----------
def load_employees():
    employees = []
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
    except FileNotFoundError:
        print("Error: employees.csv not found")
    return employees


# ---------- SAVE EMPLOYEES ----------
def save_employees(employees):
    if not employees:
        print("No data to save")
        return

    try:
        with open(CSV_FILE, "w", newline="") as file:
            fieldnames = employees[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employees)
    except Exception as e:
        print("Save error:", e)


# ---------- VIEW EMPLOYEES ----------
def view_employees():
    employees = load_employees()
    if not employees:
        print("No employees found")
        return

    for emp in employees:
        print(emp)


# ---------- ADD EMPLOYEE ----------
def add_employee():
    employees = load_employees()

    try:
        new_emp = {
            "id": input("Enter ID: "),
            "name": input("Enter Name: "),
            "age": input("Enter Age: "),
            "department": input("Enter Department: "),
            "salary": input("Enter Salary: ")
        }

        employees.append(new_emp)
        save_employees(employees)
        print("Employee added successfully")

    except Exception as e:
        print("Error:", e)


# ---------- SEARCH EMPLOYEE ----------
def search_employee():
    emp_id = input("Enter ID to search: ")
    employees = load_employees()

    for emp in employees:
        if emp["id"] == emp_id:
            print("Employee Found:", emp)
            return

    print("Employee not found")


# ---------- UPDATE EMPLOYEE ----------
def update_employee():
    emp_id = input("Enter ID to update: ")
    employees = load_employees()

    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = input("New Name: ")
            emp["age"] = input("New Age: ")
            emp["department"] = input("New Department: ")
            emp["salary"] = input("New Salary: ")

            save_employees(employees)
            print("Employee updated successfully")
            return

    print("Employee not found")


# ---------- DELETE EMPLOYEE ----------
def delete_employee():
    emp_id = input("Enter ID to delete: ")
    employees = load_employees()

    new_list = []
    for emp in employees:
        if emp["id"] != emp_id:
            new_list.append(emp)

    save_employees(new_list)
    print("Employee deleted successfully")


# ---------- REMOVE DUPLICATES ----------
def remove_duplicates():
    employees = load_employees()
    unique = {}

    for emp in employees:
        emp_id = emp["id"]
        if emp_id not in unique:
            unique[emp_id] = emp   # keep first occurrence

    cleaned_list = list(unique.values())
    save_employees(cleaned_list)
    print("Duplicate employees removed (based on ID)")


# ---------- CSV TO JSON ----------
def export_to_json():
    employees = load_employees()

    try:
        with open(JSON_FILE, "w") as file:
            json.dump(employees, file, indent=4)
        print("CSV exported to JSON successfully")
    except Exception as e:
        print("Export error:", e)


# ---------- SALARY REPORT ----------
def salary_report():
    employees = load_employees()

    if not employees:
        print("No data for report")
        return

    total_salary = 0

    for emp in employees:
        total_salary += int(emp["salary"])

    average_salary = total_salary / len(employees)

    print("Total Salary:", total_salary)
    print("Average Salary:", average_salary)


# ---------- MENU ----------
def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. View Employees")
        print("2. Add Employee")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Remove Duplicate Employees")
        print("7. Export CSV to JSON")
        print("8. Salary Report")
        print("9. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                view_employees()
            elif choice == 2:
                add_employee()
            elif choice == 3:
                search_employee()
            elif choice == 4:
                update_employee()
            elif choice == 5:
                delete_employee()
            elif choice == 6:
                remove_duplicates()
            elif choice == 7:
                export_to_json()
            elif choice == 8:
                salary_report()
            elif choice == 9:
                print("Thank you!")
                break
            else:
                print("Invalid choice, enter 1–9")

        except ValueError:
            print("Please enter numbers only (1–9)")

menu()
