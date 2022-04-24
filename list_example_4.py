list1=[10,20,30,40,50,60,70,80,90,100]
#      0  1  2  3  4  5  6  7  8  9

print(list1)
print("list1[3:8]",list1[3:8])
print("list1[2:]",list1[2:])
print("list1[:7]",list1[:7])
print("list1[3:9:2]",list1[3:9:2])

print("list1[-1]",list1[-1])
print("list1[-2]",list1[-2])

print("list1[-1:-5:-1]",list1[-1:-5:-1])
print("list1[6:1:-1]",list1[6:1:-1])
print(list1[6:-1])
print(list1[-1:6:-1])
print(list1[1:])
print("list1[::-1]",list1[::-1])

list1[3:5]=[100,200,300]
print("list1[3:5]=[100,200,300]")
print(list1)
list1[3:3]=[11,12,13,14]
print(list1)

list1=[10,20,30,40,50,60,70,80,90,100]
#      0  1  2  3  4  5  6  7  8  9
print(list1)
list1=list1[:5]+[300]+list1[5:]
print(list1)

print("sum(list1)",sum(list1))
print("max(list1)",max(list1))
print("min(list1)",min(list1))




