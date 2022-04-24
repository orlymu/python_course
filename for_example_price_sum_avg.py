sum=0
count=0

for i in range(5):
    price = int(input("enter price: "))
    sum+=price    #sum=sum+price
    count+=1      #count=count+1
    if sum>200:
        print("too expensive! We stop shopping.")
        break
else:
    print("We completed ths shopping with 5 products!")

print("sum",sum, "count",count)
print("average",sum/count)

