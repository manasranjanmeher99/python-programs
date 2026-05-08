# Find median of two sorted arrays

n1= int(input("Enter list1 no. of values: "))
n2= int(input("Enter list2 no. of values: "))

l1=[]
l2=[]

print("Enter list1 values: ")
for i in range(n1):
    str= int(input())
    l1.append(str)

print("Enter list2 values: ")
for i in range(n2):
    str1= int(input())
    l2.append(str1)

merge= sorted(l1+l2)

n= len(merge)

if n%2 == 0:
    median= (merge[n//2-1]+ merge[n//2])/2
else:
    median = merge[n//2]

print("Median:", median)