from random import randint

def init_list_random_numbers(list1:list):
    list1[:]=[randint(1,100) for i in range(20)]

    # for i in range(20):
    #     list1.append(randint(1,100))


def count_num_in_list(num:int, list1:list):
    return list1.count(num)

def location_max_num(numbers:list):
    return numbers.index(max(numbers))


# main program
list1=[]
init_list_random_numbers(list1)
print(list1)
num=int(input("enter number: "))
print(f"{num} found {count_num_in_list(num,list1)} times")
location_max_num(list1)
print(f"max number in location {location_max_num(list1)}")
