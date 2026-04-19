n= int(input("Enter the numbers of values: "))
arr=[]
for num in range(n):
    x= int(input())
    arr.append(x)
print("Before sorting the array is: ",arr)

i=1
for i in range(n):
    
    for j in range(i):
        if arr[i]< arr[j]:
            x=arr[i]
            arr[i]=arr[j]
            arr[j]=x

print("After soring the array is: ",arr)