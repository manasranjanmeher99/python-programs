#Find the first non-repeating character in a string

str= input("Enter the string: ")

for i in str:
    if str.count(i)==1:
        result= i
        break

print(f"First non repeating charcater is: {result}")