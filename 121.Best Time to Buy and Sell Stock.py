class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        ans = 0
        while i < len(prices) - 1:
            for j in range(len(prices)-1, i, -1):
                if prices[i] < prices[j]:
                    ans = max(ans, prices[j] - prices[i])
            i += 1
        return ans

    # Time complexity: O(N**2)
    # Space complexity: O(1)

    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minvalue = float("inf")
        for i, p in enumerate(prices):
            minvalue = min(p, minvalue)
            maxprofit = max(maxprofit, p - minvalue)
        return maxprofit
    # Time complexity: O(N)
    # Space complexity: O(1)
