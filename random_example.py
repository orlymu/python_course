from random import randint

num = randint(10,99)

print(num)
if num % 7 == 0 or num % 10 == 7 or num // 10 == 7:
    print("lucky number")
else:
    print("unlucky number")