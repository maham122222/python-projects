# takes func , update it and return
# decor modifies fun

def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("hello maham")
@greet
def add(a,b):
    print(a+b)

hello()
# add(4,7)
greet(add)(10,11)