# Write a program to implement multiple inheritance

class dad:
    def money(self):
        print("Dad's money")
class mom:
    def phone(self):
        print("Mom's phone")
class son(dad):
    def laptop(self):
        print("Son's laptop")

Son = son()
Son.money()
Son.phone()