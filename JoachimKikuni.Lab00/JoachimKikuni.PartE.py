##def main():
##    print(" true = prime")
##    print("false = not prime")
##    for x in range(2,n):
##        isPrime = True
##        for y in range(2,n):
##            if x%y == 0 and x != y:
##        if isPrime == True:
##            print(x, "is prime")
##        else:
##            print(x, "is not prime")
##print(main(50))

for i in range(2,50):
    isPrime = True
    for j in range(2,i):
        if i % j == 0:
            isPrime = False
            break
        if isPrime:
            print(i)
