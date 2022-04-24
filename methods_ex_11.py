def even_numbers_list(list2:list):
    for i in range(2,41,2):
        list2.append(i)

list1=[]
even_numbers_list(list1)
print(list1)