from datetime import datetime, timedelta

# Exercise 9.3
day=input("enter day: ")
month=input("enter month: ")
year=input("enter year: ")
date1=day+"/"+month+"/"+year

date2=datetime.strptime(date1,"%d/%b/%Y")
print(date2,type(date2))

# Exercise 9.4
num=int(input("enter week day number: "))
num-=2
date1=datetime.now()

print(date1)
delta=num-date1.weekday()
print(date1+timedelta(days=delta))
