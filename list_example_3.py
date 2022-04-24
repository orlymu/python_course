from random import randint
list1=[]

for i in range(5):
    num=randint(1,50)
    list1.append(num)

print(list1)

# Run over the numbers in the list.
# if we update the i, it does not affect the list
for i in list1:
    i*=2
    print(i)
print(list1)

# Run over the indexes of the numbers in the list and update
# every number in the list

for i in range(len(list1)):
    list1[i]*=2

print(list1)

