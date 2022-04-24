# digit1=int(input("enter digit 1: "))
# digit2=int(input("enter digit 2: "))
# digit3=int(input("enter digit 3: "))
#
# print(f"{digit1}{digit2}{digit3}")
#
# # 4
# # 9
# # 2
#
# num=digit1*100+digit2*10+digit3
#
# print(num, num*2)

digit1=input("enter digit 1: ")
digit2=input("enter digit 2: ")
digit3=input("enter digit 3: ")
num_str = digit1+digit2+digit3
num = int(num_str)
print(num,num*2)
print(f"{num},{num*2}")
print(str(num)+","+str(num*2))


