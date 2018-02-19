#Joachim Kikuni
#Write a third function that used dynamic programming to calculate the fibonacci numbers. Use the timer function to compare this to your other approaches.

import time

n = 600
key = [1,1]
for i in range(n):
    key.append(0)

def fib(x):

    if key[x] == 0:
        key[x] = fib(x-1)+fib(x-2)
    return key[x]

print(fib(n))

def main():
    for i in range(40, 48, 128):
        startTime = time.clock()
        fib(1)
        stopTime = time.clock()

        print ("it took", stopTime - startTime, "seconds")
