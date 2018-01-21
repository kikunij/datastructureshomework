#Joachim Kikuni
#Apples (the fruit) have become a hot commodity to trade on the stock market. Given a list of prices in chronological order, write a program that determines the greatest possible profit from a single purchase and sale of apples. Assume a starting budget of $100.

def main():
    priceList = [14, 6, 9, 7, 8, 10, 3, 9]
    length = len(priceList)
    largeDifference = 0
    highestProfit = 0.0

    for x in range (length):
        if x+1 < length and priceList[x+1] - priceList[x] > largeDifference:
            largeDifference = priceList [x+1] - priceList[x]
            highestProfit = ((100 / priceList[x]) * priceList[x+1]) - 100
            
    print ("the highest profit is:", highestProfit)

main()
