from random import randint
# a method that gets a list. The method will add a random number
# to the list.
def add_num_to_list(list1:list):
    print(id(list1))
    num=randint(1,100)
    list1.append(num)

def add_num_to_tuple(tuple1):
    print("inside add num",id(tuple1))
    num=randint(1,100)
    tuple1+=(num,)
    print(tuple1)
    print("end of add num",id(tuple1))

# new_list=[1,2,3,4,5]
# print(id(new_list))
# add_num_to_list(new_list)
# print(new_list)

def f1(a):
    a+=1
    print("a",a)

num=10
f1(num)
print("num",num)

new_tuple=(1,2,3,4,5)
print("before add num",id(new_tuple))
add_num_to_tuple(new_tuple)
print(new_tuple)