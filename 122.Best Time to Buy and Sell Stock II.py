class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        
        pointer1 = 0
        temp = prices[pointer1]
        pointer2 = 1
        ans = 0
        while pointer2 < len(prices) and pointer1 <= pointer2:
            if temp <= prices[pointer2]:
                temp = prices[pointer2]
            else:
                ans += (prices[pointer2-1] - prices[pointer1])
                pointer1 = pointer2
                temp = prices[pointer2]
            pointer2 += 1
        if temp <= prices[pointer2-1]:
            ans += (prices[pointer2-1] - prices[pointer1])
        return ans
