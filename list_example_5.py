from random import randint,choice
list1=[1,2,3,4,5,6,2,3,10]

print("list1.pop()",list1.pop())
print(list1)
print("list1.pop()",list1.pop())
print(list1)
print("list1.pop(0)",list1.pop(0))
print(list1)

list1=[1,2,3,4,5,6,2,3,10,2,3,4]
list2=list1.copy()
print("list1",list1)
print("list2",list2)
list2.append(555)
print("list1",list1)
print("list2",list2)

list1.sort()
print(list1)

list1.reverse()
print(list1)

print(choice(list1))



