dict1={"maham":34, "hayyan":77}
print(dict1['hayyan'])

dict1["esha"]=88
print(dict1)
print(dict1.get("esha"))

num =int(input("enter num"))
for i in range(1,11):
    product=num*i
    print(f"{num} x {i} = {product}")
