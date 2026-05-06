# Count frequency of each character in a string

str= input("Enter the string:")
dict={}
for char in str:
    if char in dict:
        dict[char]+=1
    else:
        dict[char]=1

print("Character frequencies:")
for char in dict:
    print(f"{char}: {dict[char]}")
    