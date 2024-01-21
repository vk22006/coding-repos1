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