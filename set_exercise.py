from random import randint

# set1=set()
#
# while len(set1)<6:
#     num=randint(1,10)
#     set1.add(num)
#
# print(set1)
#
# for i in set1:
#     print(i)
#
# if 8 in set1:
#     print("8 exists")
#
# #set1.clear()
# set1=set()
# print(set1)

set1={1,2,3,4}
set2={4,5,6,7}
set3=set()

for i in set1:
    set3.add(i)
for i in set2:
    set3.add(i)

print(set3)


