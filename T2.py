from random import randint
list1=[randint(1,100) for i in range(10)]
list2=[randint(1,100) for i in range(10)]

print(list1)
print(list2)

for i in list1:
    if i in list2:
        print("there is at least one common number")
        break
else:
    print("there are no numbers")
