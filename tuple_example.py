tup1=(1,2,3,4,5,"abc",7.6)
tup2=1,2,3,4,5,"abc",7.6

tup3=()
print("tup1",tup1)
print("tup1[2]",tup1[2])

tup1+=10,20,30
print(tup1)

tup1+=40,
print(tup1)

list1=[1,2,3,4]
print(tuple(list1))

tup1=(1,2,3,4)
list1=list(tup1)
list1[0]=10
tup1=tuple(list1)
print(tup1)

for i in tup1:
    print(i)

if 10 in tup1:
    print("10 found")

a,b,c=10,20,30

print(a,b,c)

a,b=b,a
print(a,b)

tup1=(11,12,13)
a,b,c=tup1
print(a,b,c)

tup2=(a,b,c)
print(tup2)

tup3=tup2
print("tup2",tup2)
print("tup3",tup3)
tup3+=(50,)
print("tup2",tup2)
print("tup3",tup3)

