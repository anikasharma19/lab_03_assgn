class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, target_age):
        result = [emp for emp in self.employees if emp.age == target_age]
        return result

    def search_by_name(self, target_name):
        result = [emp for emp in self.employees if emp.name == target_name]
        return result

    def search_by_salary(self, operator, target_salary):
        if operator == "<":
            result = [emp for emp in self.employees if emp.salary < target_salary]
        elif operator == "<=":
            result = [emp for emp in self.employees if emp.salary <= target_salary]
        elif operator == ">":
            result = [emp for emp in self.employees if emp.salary > target_salary]
        elif operator == ">=":
            result = [emp for emp in self.employees if emp.salary >= target_salary]
        else:
            result = []
        return result

def main():
    table = EmployeeTable()

    emp_data = [
        ("161E90", "Raman", 41, 56000),
        ("161F91", "Himadri", 38, 67500),
        ("161F99", "Jaya", 51, 82100),
        ("171E20", "Tejas", 30, 55000),
        ("171G30", "Ajay", 45, 44000)
    ]

    for emp_id, name, age, salary in emp_data:
        employee = Employee(emp_id, name, age, salary)
        table.add_employee(employee)

    print("Search Options:")
    print("1. Age\n2. Name\n3. Salary")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        target_age = int(input("Enter age to search: "))
        result = table.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter name to search: ")
        result = table.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter operator (<, >, <=, >=): ")
        target_salary = int(input("Enter salary to search: "))
        result = table.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")
        return

    if result:
        print("\nSearch Results:")
        for emp in result:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching records found.")

if __name__ == "__main__":
    main()
