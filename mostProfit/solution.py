class Solution(object):
    def maxProfit(self, prices):
        # set buy price to first price in array
        price = prices[0]
        profit = 0

        # iterate through the rest of the list, replacing buy price if we find a better one
        for p in prices[1:]:
            if p < price:
                price = p
            
            # profit resets if we encounter a buy price that will up our profit margin
            profit = max(profit, p - price)
        
        # return profit as per instruction
        return profit

solution = Solution()
input = [7,1,5,3,6,4]

print(solution.maxProfit(input))