# class Person:
#     name="maham"
#     age=22


# a=Person()
# print(a.name)


# constructor
# cons initialize class objects
# it is invoked automatically
class Person:

    def __init__(self , n, o):
        self.name=n
        self.occ=o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a=Person("harry", "developer")
b=Person("maham", "full stack developer")
a.info()
b.info()