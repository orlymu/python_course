from random import randint

# [[11,6],[56,4],[10,56].........]

list1=[]

# for i in range(10):
#     numbers=[]
#     for j in range(2):
#         numbers.append(randint(1,100))
#     list1.append(numbers)

# for i in range(10):
#     list1.append([])
#     for j in range(2):
#         list1[i].append(randint(1,100))

for i in range(10):
    numbers=[randint(1,100) for j in range(2)]
    list1.append(numbers)

print(list1)

for item in list1:
    for i in item:
        if i%3==0:
            print(item)
            break

print("=================================================")
for item in list1:
    if item[0]%3==0 and item[1]%3==0:
        print(item)

print("=================================================")
for item in list1:
    for i in item:
        if i%3!=0:
            break
    else:
        print(item)