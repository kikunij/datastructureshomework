#Joachim Kikuni
#Write a python program that asks the user to enter a positive integer and calls a recursive function that returns the number of steps it takes to reach 1.

##number = int(input("enter a positive number:"))

def collatz(number, x):

    steps = x
    
    if number == 1:
        steps += 1
        print("It tatkes", steps, "steps.")
        return 1
    else:
        if number%2 == 0:
            steps += 1
            return collatz(number/2, steps)
        else:
            steps += 1
            return collatz((number*3)+1, steps)

def main():
    num = eval(input("Enter a positive integer:"))
    collatz(num, 0)


