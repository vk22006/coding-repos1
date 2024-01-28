# Write a program to implement hierachial inheritance

class Dad():
    def money(self):
        print("Dad's money")
class Son1(Dad):
    pass
class Son2(Dad):
    pass
class Son3(Dad):
    pass

s1 = Son1()
s2 = Son2()
s3 = Son3()

s1.money()
s2.money()
s3.money()