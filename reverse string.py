# Reverse the string without using slicing

str= input("Enter the string: ")
rev_str=""
len= len(str)
for i in str:
    rev_str+= str[len-1]
    len-=1
print("Reverse string is:", rev_str)
