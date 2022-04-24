from random import randint
list1=[]

for i in range(20):
    num=randint(1,50)
    list1.append(num)

print(list1)

num_to_delete=int(input("enter number to delete: "))

#while list1.count(num_to_delete)>0:
while num_to_delete in list1:
    list1.remove(num_to_delete)

print(list1)

# if 20 in list1:
#     i=list1.index(20)
#     list1[i]+=5
# else:
#     print("20 not in the list")
#
# print(list1)
#
# for i in list1:
#     if i%3==0:
#         print(i)
#

if 1 not in list1:
    pass








