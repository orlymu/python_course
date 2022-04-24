from random import randint

# A method average will get 2 numbers and return the average
def average(a:int,b:int):
    return (a+b)/2

# A method that gets 2 random numbers and returns the average
def average_2_random():
    num1=randint(1,100)
    num2=randint(1,100)
    avg=average(num1,num2)
    return avg

# A method calc_numbers that gets 2 numbers and returns:
# sum,diff,mult,div
def calc_numbers(a,b):
    sum=a+b
    diff=a-b
    mult=a*b
    div=a/b
    return sum,diff,mult,div

# A method calc_numbers that gets 2 numbers and prints:
# sum,diff,mult,div and returns nothing
def calc_numbers_2(a,b):
    sum=a+b
    diff=a-b
    mult=a*b
    div=a/b
    print(sum,diff,mult,div)

calc_numbers_2(8,3)

# A method that gets a number as input from the user and returns it
# if the user reached 5 trials, returns 0
def get_number():
    num=input("enter number: ")
    count=0
    while not num.isnumeric():
        count+=1
        if count==5:
            return 0
        num = input("Invalid number! try again: ")
    return int(num)

# a method that gets a number and returns if
# it's a valid grade or not (0-100)
def valid_grade(grade):
    if 0<=grade<=100:
        return True
    else:
        return False


num1=get_number()
if valid_grade(num1):
    print("valid grade")
else:
    print("invalid grade")

num2=get_number()
if valid_grade(num2):
    print("valid grade")
else:
    print("invalid grade")


print(average(num1,15))
# avg = average(num1,num2)
# if num1>avg:
#     print(num1)
# else:
#     print(num2)

if num1>average(num1,num2):
    print(num1)
else:
    print(num2)

result = calc_numbers(7,3)
print(result, type(result))