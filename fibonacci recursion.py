# Generate Fibonacci using recursion + memorization

memo={}
def Fibonacci(n):
    if n in memo:
        return memo[n]
    
    if n<=1:
        return n
    
    memo[n]= Fibonacci(n-1)+Fibonacci(n-2)

    return memo[n]





terms= int(input("Number's of terms: "))

for i in range(terms):
    print(Fibonacci(i), end=" ")
