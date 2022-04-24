text="shalom 123shalom"
#     0123456789

print(text[2])
print(len(text))
print("text.count('sh')",text.count("sh"))
print("text.index('sh')",text.index("sh",4))

if "sh" in text:
    print("yes")
else:
    print("no")

for i in text:
    print(i, end=" ")

print()

sentence=input("enter a sentence: ")
print(sentence.split(' '))

# list1=input("enter a list of values with spaces: ").split()
# print(list1)

