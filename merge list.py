# Merge two sorted lists

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

merge=[]
i=0
j=0


while i < len(l1) and j < len(l2):

    if l1[i] < l2[j]:
        merge.append(l1[i])
        i += 1
    else:
        merge.append(l2[j])
        j += 1

while i < len(l1):
    merge.append(l1[i])
    i += 1

while j < len(l2):
    merge.append(l2[j])
    j += 1

print(merge)