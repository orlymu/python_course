from random import randint

grades=[]
num_of_grades=int(input("enter number of grades: "))

for i in range(num_of_grades):
    #grades.append(int(input("enter grade: ")))
    grades.append(randint(20,100))

print(grades)

passed_grades=[]
failed_grades=[]
count_pass=0
count_fail=0
for grade in grades:
    if grade>=70:
        passed_grades.append(grade)
        count_pass+=1
    else:
        failed_grades.append(grade)
        count_fail+=1

print("failed:",count_fail,"passed:",count_pass)
print(passed_grades,failed_grades)
print("failed:",len(failed_grades),"passed:",len(passed_grades))