print("====== Employee Payroll System ======")

FILE_NAME = "employees.txt"

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        """This method will be overridden in subclasses"""
        pass

    def to_file_string(self):
        """Convert object data into file format"""
        pass


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def to_file_string(self):
        return f"FullTime,{self.emp_id},{self.name},{self.monthly_salary}"


class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

    def to_file_string(self):
        return f"PartTime,{self.emp_id},{self.name},{self.hours_worked},{self.hourly_rate}"


class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee added successfully.")

    def save_to_file(self):
        try:
            with open(FILE_NAME, "w") as file:
                for emp in self.employees:
                    file.write(emp.to_file_string() + "\n")
            print("Employees saved to file.")
        except Exception as e:
            print("Error saving file:", e)

    def load_from_file(self):
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    if data[0] == "FullTime":
                        emp = FullTimeEmployee(data[1], data[2], float(data[3]))
                    elif data[0] == "PartTime":
                        emp = PartTimeEmployee(
                            data[1], data[2], float(data[3]), float(data[4])
                        )
                    else:
                        continue

                    self.employees.append(emp)

            print("Employees loaded from file.")

        except FileNotFoundError:
            print("No employee file found.")
        except Exception as e:
            print("Error loading file:", e)

    def display_payroll(self):
        print("\n--- Payroll Details ---")
        for emp in self.employees:
            print(f"ID: {emp.emp_id}")
            print(f"Name: {emp.name}")
            print(f"Salary: ₹{emp.calculate_salary():.2f}")
            print("-" * 30)


if __name__ == "__main__":

    payroll = PayrollSystem()

    emp1 = FullTimeEmployee("E101", "Shiv", 50000)
    emp2 = PartTimeEmployee("E102", "Rahul", 80, 500)

    payroll.add_employee(emp1)
    payroll.add_employee(emp2)

    payroll.display_payroll()

    payroll.save_to_file()

    print("\nReloading from file...")
    new_payroll = PayrollSystem()
    new_payroll.load_from_file()
    new_payroll.display_payroll()