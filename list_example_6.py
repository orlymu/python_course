from random import randint

# list1=[]
#
# for i in range(1,11):
#     list1.append(i)
#
# print(list1)

list1=[i*2 for i in range(1,11)]
print(list1)

list1=[int(input("enter value: ")) for i in range(4)]
print(list1)

list1=[randint(1,100) for i in range(20)]
print(list1)