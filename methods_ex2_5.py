def convert_to_list(items):
    #if type(items)==str or type(items)==dict or type(items)==tuple or type(items)==set:
    if type(items) in [str,dict,tuple,set]:
        list1=[i for i in items]
        return list1
    else:
        print("invalid type")
        return None

print(convert_to_list((1,2,3,4,5)))
print(convert_to_list({1,2,3,4,5}))
print(convert_to_list("abcd123"))
print(convert_to_list({1:10,2:20,3:30,4:40}))
print(convert_to_list(50))
