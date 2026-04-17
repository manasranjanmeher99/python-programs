# x= int(input("number of terms: "))
'''a=0
b=1
 f x<=0:
    print("Please enter a positive integer")
elif x==1:
    print("Fibonacci sequence upto",x,":")
    print(a)
else:
    print("Fibonacci sequence:")
    for i in range(x):
        print(a)
        c=a+b
        a=b
        b=c '''

a=0
b=1
n=int(input("Enter a number:"))
nr=1
if n<=0 and n<=1:
    print("Enter a greater number than 1")
else :
    while nr<n:
        c=a+b
        a=b
        b=c
        nr=b

print(f"Next nearest numbers of {n} is: {nr}")
