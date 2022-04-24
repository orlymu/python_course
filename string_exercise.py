# Get a string as input
# Create a new string that contains all the characters from the original string
# that are not digits

text=input("enter text: ")

new_text=""

for i in text:
    if not i.isnumeric():
        new_text+=i

print(new_text)



