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
    prices=list(map(int,input('Enter prices of each day:').split()))
    print('Max Profit:',buyAndSellStock(prices))
main()