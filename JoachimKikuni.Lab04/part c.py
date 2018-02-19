import time
array = [1,2]
def fibonacci(n):
    if n == 0:
        return 1
    elif n == len(array):
        return array(n-1)
    else:
        temp = fibonacci(n-1) + fibonacci(n-2)
        array.append(temp)
        return temp
def main():
    for i in range(30, 100, 10):
        startTime = time.clock()
        fibonacci(1)
        sleepTime = time.clock()
        print ("it took", stopTime - startTime, "seconds")
