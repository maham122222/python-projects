class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show(self):
        print(f"The name of Employee  : {self.id} is {self.name}")

class Programmer(Employee):
    def lang(self):
        print("The default language is python")


e1=Employee("maham", 778)
e1.show()

e2=Programmer("hassan",6767)
e2.show()
e2.lang()


    