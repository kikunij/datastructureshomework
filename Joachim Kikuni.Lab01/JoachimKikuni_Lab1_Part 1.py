#Joachim Kikuni
#Write a program that plays the game of FizzBuzz: Count from 1 to 100, but when the number is a multiple of 3, say 'Fizz', and when the number is a multiple of 5, say 'Buzz'. When the number is a multiple of both, say 'FizzBuzz'


def main():
    i = 1
    while (i <= 100):
        if i % 3==0:
            print ("Fizz")
        elif i % 5==0:
            print ("Buzz")
        elif i % 3==0 and 5==0:
            print("FizzBuzz")
        else:
            print(i)

        i +=1
main()
            
