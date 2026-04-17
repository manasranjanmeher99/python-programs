import math
n=int(input("Enter a number: "))

one_digit=["one","two","three","four","five","six","seven","eight","nine"]

two_digits=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]    
tens=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
tens_power=["hundred","thousand"]   

if n<10:
    print(one_digit[n-1])
elif n<20:
    print(two_digits[n-10])
elif n<100:
    print(tens[n//10-2],end=" ")
    if(n%10!=0):
        print(" ",end=" ")
        print(one_digit[n%10-1])
elif n<1000:
    x=n//100
    print(one_digit[x-1],tens_power[0],end=" ")
    r=n%100
    if(r<10 and r>0):
        print(one_digit[r-1])
    elif(r<20 and r>=10):
        print(two_digits[r-10])
    elif r>20:
        print(tens[r//10-2], end=" ")
        if(r%10!=0):
            print(one_digit[r%10-1])
    else:
        print(" ")
else:
    a=n//1000
    if a<10:
        print(one_digit[a-1],tens_power[1], end=" ")
    elif a>=10 and a<20:
        print(two_digits[a-10],tens_power[1],end=" ")
    else:
        print(tens[a//10-2],end=" ")
        if(a%10!=0):
            print(one_digit[a%10-1],tens_power[1],end=" ")
    rem=n%1000
    x=rem//100
    print(one_digit[x-1],tens_power[0],end=" ")
    r=n%100
    if(r<10 and r>0):
        print(one_digit[r-1])
    elif(r<20 and r>=10):
        print(two_digits[r-10])
    elif r>20:
        print(tens[r//10-2], end=" ")
        if(r%10!=0):
            print(one_digit[r%10-1])
    else:
        print(" ")
