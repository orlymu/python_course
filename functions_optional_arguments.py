# a function that receives a grade

def is_passed_grade(grade,passed_grade=70):
    if grade>=passed_grade:
        return True
    else:
        return False

def avg(num1,num2,*numbers):
    sum_numbers=num1+num2+sum(numbers)
    count_numbers=len(numbers)+2
    return sum_numbers/count_numbers

def avg2(*numbers):
    if len(numbers)>0:
        return sum(numbers)/len(numbers)
    else:
        return 0

def print_details(id,name,age,**extra_details):
    print("id",id)
    print("name",name)
    print("age",age)
    for i in extra_details:
        print(i,extra_details[i])
    print("------------------------------------------------")

def print_details_2(id,name,age,country="Israel",*children,**extra_details):
    print("id",id)
    print("name",name)
    print("age",age)
    print("country",country)
    print(children)
    for i in extra_details:
        print(i,extra_details[i])
    print("------------------------------------------------")

print_details(123,"david",45)
print_details(123,"david",45)
print_details(123,"david",45,address="ben yehuda 30 tel aviv",phone="01234567")
print_details_2(123,"david",45,"USA")
print_details_2(123,"david",45,"aaa","bbb","ccc",address="ben yehuda 30 tel aviv",phone="01234567")
print_details_2(123,"david",45,"China","aaa","bbb","ccc",address="ben yehuda 30 tel aviv",phone="01234567")
print_details_2(123,"david",45,address="ben yehuda 30 tel aviv",phone="01234567")
print("=============================================")
# grade=int(input("enter grade: "))
# print(is_passed_grade(grade,60))
# print(is_passed_grade(grade))

print("===========================================")

print(avg(9,8))
print(avg(9,8,10,11,12,13))
print(avg(9,8,10))




