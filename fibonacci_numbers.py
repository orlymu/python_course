# Get a size of a fibonacci numbers and print the numbers

num = int(input("enter number of fibonacci numbers: "))

number1=0
number2=1

print(number1,end=" ")
print(number2,end=" ")

# 0 1 1 2 3 5 8

for i in range(num-2):
    number3 = number1 + number2
    print(number3,end=" ")
    number1=number2
    number2=number3


