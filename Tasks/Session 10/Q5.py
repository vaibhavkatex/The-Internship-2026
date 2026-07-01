# Create a class Employee
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

    def give_raise(self, amount):
        self.salary += amount
        print("New Salary after raise:", self.salary)

    def yearly_bonus(self):
        return self.salary * 0.10


# Create an employee object
emp1 = Employee("Gangadhar", 76000)

# Demonstrate all methods
emp1.display_details()

emp1.give_raise(5000)

bonus = emp1.yearly_bonus()
print("Yearly Bonus:", bonus)