# Write a program to implement multi-level inheritance

class grandpa:
    def money(self):
        print("Grandpa's money")
class dad(grandpa):
    def phone(self):
        print("Dad's phone")
class son(dad):
    def laptop(self):
        print("Son's laptop")

Son = son()
Dad = dad()

Son.phone()
Dad.money()
Son.money()