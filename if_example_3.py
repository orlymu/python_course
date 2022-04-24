grade=int(input("enter grade: "))

#if grade>=0 and grade<=100:
if 0<=grade<=100:
    print("valid grade")
else:
    print("invalid grade")

if grade<0 or grade>100:
    print("invalid grade")
else:
    print("valid grade")

