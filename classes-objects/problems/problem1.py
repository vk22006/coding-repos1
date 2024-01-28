# Problem - 1
# -----------
# Create a base class called employee with properties name and salary.
# Create a derived class called manager that inherits from employee and adds a property department.
# Write a method in manager to display the name, salary, and department of the manager.


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
    def display(self):
        print(self.name,self.salary,self.department)
        
manager = Manager("Anirudh",80000,"Software engineer")
manager.display()
