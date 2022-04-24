def average(a,b,*numbers):
    print(numbers)
    if len(numbers)>0:
        print("first index in args",numbers[0])
    return a+b+sum(numbers)/(2+len(numbers))

def average_2(*numbers):
    print(numbers)
    return sum(numbers)/len(numbers)

avg = average(5,6,7,8,9)
print(avg)

#======================================================
# {phone:0551234567, address:"yafo 57 tel aviv"}
def print_details(name,age,**extra_details):
    print(f"name:{name} age:{age}", end=" ")
    #print(extra_details)
    for i in extra_details:
        print(f"{i}:{extra_details[i]}",end=" ")
    print()

def print_details_children(name,age,*children,**extra_details):
    print(f"name:{name} age:{age}", end=" ")
    for i in children:
        print(i,end=' ')
    print()
    #print(extra_details)
    for i in extra_details:
        print(f"{i}:{extra_details[i]}",end=" ")


print_details("dan",30,phone="0541234567",
              address="yafo 57 tel aviv",email="abc@gmail.com")
print_details_children("dan",30,"aaa","bbb",phone="0541234567",
                address="yafo 57 tel aviv",email="abc@gmail.com")

#======================================================
def print_details_salary(name,age,salary=0,*args):
    print("====================")
    print(args)
    print(name,age,salary)

def f(*args,num=5):
    print(num,args)

print()


print_details_salary("dani",15)
print_details_salary("dani",15,2000,2,3,4,5)
print_details_salary(age=30,salary=5000,name="gadi")

f(1,2,3,4,5,num=10)
f(1,2,3,4,5)



