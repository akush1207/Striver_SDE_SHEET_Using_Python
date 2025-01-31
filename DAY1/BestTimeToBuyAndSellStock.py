from typing import List
def buyAndSellStock(prices:List[int]) -> int:
    maxProfit=0
    minPrice=prices[0]
    for price in prices[1:]:
        if price<minPrice:
            minPrice=price
        else:
            maxProfit=max(maxProfit,price-minPrice)            
    return maxProfit
def main():
    num=(int(input('Enter the no. of days:')))
    prices=[]
    print('Enter prices of each day:')
    for i in range(num):
        prices.append(int(input()))
    print('Max Profit:',buyAndSellStock(prices))
main()