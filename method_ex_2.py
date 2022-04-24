def is_3_digits(a):
    if 100<=a<=999:
        return True
    else:
        return False


num=int(input("enter number: "))

if is_3_digits(num):
    print("it's 3 digits")
else:
    print("it's not 3 digits")