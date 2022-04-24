from random import randint

list1=[randint(1,100) for i in range(20)]

print(list1)

list_div_3=[]

for i in list1:
    if i%3==0:
        list_div_3.append(i)

print(list_div_3)

for i in list_div_3:
    list1.remove(i)

print(list1)

