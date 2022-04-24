def remove_from_list(list1:list,item):
    # [1,2,3,4,5]
    item_location=list1.index(item)
    list1[item_location:item_location+1]=[]
    return list1

list1=[1,2,3,4,5,4]
remove_from_list(list1,4)
print(list1)
