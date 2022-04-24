from random import randint

# A method average will get 2 numbers and return the average
def average(a:int,b:int):
    return (a+b)/2

# A method that gets a number as input from the user and returns it
# if the user reached 5 trials, returns 0
def get_number():
    """get a valid number from the user"""
    num=input("enter number: ")
    count=0
    while not num.isnumeric():
        count+=1
        if count==5:
            return 0
        num = input("Invalid number! try again: ")
    return int(num)

# A method calc_numbers that gets 2 numbers and returns:
# sum,diff,mult,div
def calc_numbers(a,b):
    sum=a+b
    diff=a-b
    mult=a*b
    div=a/b
    return sum,diff,mult,div