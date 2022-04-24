d1={1:10,2:20,3:30,4:40,"abc":600,8.5:[1,2,3]}

d1={1:20}
# key=1   value=20

grades={"shlomi":70,"gadi":90,"gila":75,"sarit":80,"dani":80}

print(grades)
print("grades['gila']",grades["gila"])
# add "hana":60 to the dictionary
grades["hana"]=60
print(grades)
#update the value of the key "shlomi" to 75
grades["shlomi"]=75
print(grades)

del grades["gadi"]
print(grades)

print("len(grades)",len(grades))
print("max(grades)",max(grades))

for i in grades:
    print(i, grades[i])

if "gila" in grades:
    print("gila found")

print("grades.keys()",list(grades.keys()))
print("grades.values()",list(grades.values()))
print("grades.items()",list(grades.items()))

grades.update({"aaa":70,"bbb":40})
grades.update({"ccc":90})
print(grades)










