class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Max profit will be zero in starting and Minprice price will be anything out of range of 10^4
        
        maxprofit = 0
        minpricetillnow = 9999999
        
        #Loop Through all the prices
        
        for price in prices:
            
            #Update maxprofit with max of maxprofit or diff. of price and minpricetillnow
            maxprofit = max(maxprofit,price - minpricetillnow)
            #Update minpricetillnow (Minpricetillnow will be updated with the lowest value in the end)
            minpricetillnow = min(price,minpricetillnow)
        
        #Return MaxProfit
        return maxprofit