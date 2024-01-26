# Create class called student and create variables name and register number using constructor.
# Add a function display to print the name and register number of the students
# TASK: Pass the name and reg no through the object

class student:
    def __init__(self,name,regno):
        self.name = name
        self.regno = regno
    def display(self):
        print("Name: ",self.name)
        print("Register no: ",self.regno)

s1 = student("Monish",1001)
s2 = student("Arun",1002)

s1.display()
s2.display()
