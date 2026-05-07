# Print Pascal’s Triangle

n= int(input("Enter the numbers of rows: "))

for i in range(n):
    num=1
    #space print
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(num,end=" ")
        num=num * (i-j)//(j+1)
    
    print()