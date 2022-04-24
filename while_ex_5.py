num=int(input("enter number: "))

while 9<num<100:
    if num%7==0 or num%10==7 or num//10==7:
        print("lucky number")
    else:
        print("unlucky number")

    num = int(input("enter number: "))

print("invalid number")