# Remove duplicates from a list without using set()
n= int(input("Enter the  number of input:"))
arr=[]

print("enter array: ")
for i in range(n):
    ele= int(input())
    arr.append(ele)

unique_arr=[]
for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)

print("The list after removing duplicates is: ", unique_arr)