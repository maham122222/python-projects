class Employee:
    # contructor
    def __init__(self,n,a,s):
        self._name=n
        self._age=a
        self._salary=s
    
    @property
    def emp(self):
        return self._name,self._age,self._salary

    @emp.setter
    def emp(self,new_name,new_age,new_salary):
        self._name=new_name
        self._age=new_age
        self._salary=new_salary

    def show(self):
        print(f"{self._name}'s age is {self._age} and her salary is {self._salary}")

        
obj1=Employee("maham",33,66)
obj1._name="maham"
obj1._age=22
obj1._salary=3000000
obj1.show()
        