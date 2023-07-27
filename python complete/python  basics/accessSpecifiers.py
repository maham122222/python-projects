# private , protected, public
# name mangling-> used to protect class private 
# and subclass private attributes
# from being accidently written by subclass
# accessed by a._className__obj

class Student:
    def __init__(self):
        self.__name="maham"
        self._id=89

a=Student()

# private things can be accessed like this
print(a._Student__name)


# protected can be used by class itseldf and by its subclass
print(a._id)
