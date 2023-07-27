def funargs(*args, **kwargs):
    for items in args:
        print(items)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")


list=["maham", "hayyan", "esha","amna","jamil"]
list2={"bushra":"dev","sarmad":"mechanic"}
funargs(*list, **list2)