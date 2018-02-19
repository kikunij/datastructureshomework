def Fibonacci(n):
    if n<0:
        print("invalid number")
    elif n==1 or n==0:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
for n in range (0,10):  
    print(n, ":", Fibonacci(n))
