# Find the second largest number in a list

n= int(input("Enter the  number of input:"))
arr=[]
print("enter array: ")
for i in range(n):
    ele= int(input())
    arr.append(ele)

arr.sort()
print("The second largest value of list is: ",arr[n-2])
    