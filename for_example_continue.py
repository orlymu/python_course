sum=0
count=0

for i in range(5):
    price = int(input("enter price: "))

    if sum+price>200:
        print("too expensive! I don't want this product.")
        continue

    sum += price  # sum=sum+price
    count += 1  # count=count+1

print("sum",sum, "count",count)
print("average",sum/count)