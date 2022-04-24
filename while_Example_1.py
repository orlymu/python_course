# grade=int(input("enter grade: "))
#
# while grade<0 or grade>100:
#     print("invalid grade")
#     grade = int(input("enter grade: "))
#
# if grade>=70:
#     print("passed")
# else:
#     print("failed")

# we get grades from the user until the grade is -1
# for every grade - we print passed/failed
grade=int(input("enter grade: "))
sum=0
count=0

while grade!=-1:
    sum+=grade
    count+=1

    if grade >= 70:
        print("passed")
    else:
        print("failed")

    if grade==0:
        print("we got a zero grade. we exit.")
        break

    grade = int(input("enter grade: "))
else:
    print("No zero grades")

print("the grades input is done!")
print("average",sum/count)

