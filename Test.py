year=int(input("enter year: "))
day=8
month=12

if year%100>=10:
    print(year%100)
else:
    print(f"0{year%100}")

#2021
print(f"{day}/{month}/{year//10%10}{year%10}")

