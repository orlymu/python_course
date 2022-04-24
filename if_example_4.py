name=input("enter student name: ")

if name=="":
    name="no name"

grade=input("enter grade: ")
if grade=='':
    grade=0
else:
    grade=int(grade)

if grade>=70 and (name=="George" or name=="Michael"):
    print(name,"passed")
else:
    print(name,"failed")

