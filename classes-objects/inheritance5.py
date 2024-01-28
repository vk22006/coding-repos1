# Write a program to implement hybrid inheritance

class Dad():
    def money(self):
        print("Dad's money")
class Land():
    def important(self):
        print("Important land")
class Son1(Dad,Land):
    pass
class Son2(Dad):
    pass
class Son3(Dad):
    pass

s1 = Son1()
s1.Dad()
s1.Land()