# Implement binary search

'''n= int(input("Enter the number of values:"))
arr=[]
for i in range(n):
    ele= int(input())
    arr.append(ele)'''

def binary_search(arr,left,right,search):
    if left>right:
        return -1

    mid = (left+ right)//2
    if arr[mid]== search:
        return mid
    elif arr[mid]< search:
        return binary_search(arr, mid+1,right, search)
    else:
        return binary_search(arr,left, mid-1, search)

arr=[2,4,6,8,9,11,13]
print(arr)
print("Index no: ",binary_search(arr, 0, len(arr)-1, 11))