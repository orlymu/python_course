a=50

list1=[10,11,12,13,"aa","bb",100,5.4,35,a,100,35]
#      0  1  2  3   4    5   6   7
a=45
print(list1)
print("list1[2]",list1[2])
list1[3]=30
print(list1)
list1[3]=list1[2]*2
list1[3]+=2
print(list1)

list1.append(100)
list1+=[100]
print(list1)
list1+=[1,2,3,4]
print(list1)
list2=[20,21,22,23]
list1+=list2
print(list1,list2)


print("list2*3",list2*3)
print("len(list2*3)",len(list2*3))
print("len(list1)",len(list1))

print("list1.count(100)",list1.count(100))
print(list1)
print("list1.index(35)",list1.index(35))
i=list1.index(35)
list1[i]*=2
print(list1)

print("list1.remove(100)")
list1.remove(100)
print(list1)
del list1[0]
print("del list1[0]")
print(list1)


for i in range(len(list1)):
    if list1[i]==100:
        print(i)







