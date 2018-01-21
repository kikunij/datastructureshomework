#Joachim Kikuni
#Write a python program that asks the user to enter the name of a text file, then produces a text file with the same content but line numbers added to the beginning of each line. 

def main():
    
    file = open(input("enter the name of a text file:"))
    text = file.readlines()
    lineNumber = 1

    for line in text:
        print(lineNumber, line)
        lineNumber +=1

        file.close
        
    
main()
