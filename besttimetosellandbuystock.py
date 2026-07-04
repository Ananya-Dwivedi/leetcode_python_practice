class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        min_price=prices[0]
        if not prices:
            return 0
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            profit=prices[i]-min_price
            if profit >max_profit:
                max_profit=profit
        return max_profit




if __name__ == "__main__": 
    result=Solution()
    prices = [7,1,5,3,6,4] 
    
    output=result.maxProfit(prices)
    print(output)  