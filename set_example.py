from random import randint

set1={1,2,3,4,5,6}
print(set1)
set2=set()
print(set2)

set1.add(7)
print(set1)

set1.remove(4)
print(set1)

set1.discard(50)
print(set1)

set1.add("abc")
print(set1)

set1.add((1,2,3))
print(set1)

set1.add(1)
print(set1)

print(set1.pop())
print(set1)

list1=[randint(1,10) for i in range(15)]
print(list1)

set3=set(list1)
print(set3)

list1=list(set3)
print(list1)

# list1=list(set(list1))
# print(list1)