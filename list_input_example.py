# list1=input("enter text: ").split()
# print(list1)
#
# list1=list(input("enter text: "))
# print(list1)



value=input("enter value: ")
# list1=[]
# for i in value:
#     if i.isnumeric():
#         list1.append(int(i))

list1=[int(i)  for i in value if i.isnumeric()]
print(list1)
