#Joachim Kikuni
#Write a python function that Recursively calculates the nth fibonacci number. The fibonacci sequence is defined as:

def Fibonacci(n):
    if n<0:
        print("invalid number")
    elif n==1 or n==0:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
for n in range (0,100):  
    print(n, ":", Fibonacci(n))
