num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))

print(num1/num2)
print(num1//num2)
print(num1%num2)

# 53
num3=int(input("enter 3 digits number: "))
print(num3%10)     # right digit
print(num3//10%10) # middle digit
print(num3%100//10)
print(num3//100)   # left digit
