class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

class HourlyEmployee(Employee):
    """
    An HourlyEmployee has an hourly wage.
    """
    def __init__(self, name, wage):
        super().__init__(name)

        self.hourly_wage = wage

    def display(self):
        print(self.name + " - $" + self.hourly_wage + "/hour")

class SalaryEmployee(Employee):
    """
    A SalaryEmployee has a salary.
    """
    def __init__(self, name, salary):
        super().__init__(name)

        self.salary = salary

    def display(self):
        print(self.name + " - $" + self.salary + "/year")

def main():
    """
    Prompt the user for a series of employees and then display
    their information at the end.
    """
    employees = []

    command = ""

    while command != "q":
        command = input("Enter 'h' (hourly employee), 's', (salary employee) or 'q': ")

        if command == "h":
            name = input("Enter name: ")
            wage = int(input("Enter wage: "))

            emp = HourlyEmployee(name, wage)
            employees.append(emp)
        elif command == "s":
            name = input("Enter name: ")
            salary = int(input("Enter salary: "))

            emp = SalaryEmployee(name, salary)
            employees.append(emp)

    # We are done entering data, print them out now

    for employee in employees:
        print(employee)

if __name__ == "__main__":
    main()