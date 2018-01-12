#Joachim Kikuni
#Write a program that reads a text file and outputs the text file with line numbers at the beginning of each line.

def main():
    file = open("poem.txt", "r")
    text = file.readlines()
    lineNumber = 1

    for line in text:
        print(lineNumber, line)
        lineNumber += 1

    file.close
main()
