from random import randint

# i=1
#
# while i<=5:
#
#     num = randint(10, 99)
#     print("i", i,"num",num)
#
#     if num%7==0 or num%10==7 or num//10==7:
#         print("lucky number")
#     else:
#         print("unlucky number")
#
#     i+=1

# 0,1,2,3,4
for i in range(5):
    num = randint(10, 99)
    print("i", i,"num",num)

    if num%7==0 or num%10==7 or num//10==7:
        print("lucky number")
    else:
        print("unlucky number")