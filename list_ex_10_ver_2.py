from random import randint

list1 = [randint(1, 100) for i in range(20)]

print(list1)

list2=[]

for i in list1:
    if i%3!=0:
        list2.append(i)

list1=list2
print(list1)
