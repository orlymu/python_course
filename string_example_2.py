value = input("enter value: ")

print(value.find("abc",3))
print(value.count("c"))

value = input("enter value: ")
if value.isnumeric():
    value=int(value)
else:
    print("invalid number")

value = input("enter value: ")
print(value.isupper())
print(value.islower())
print(value[0].isupper())





