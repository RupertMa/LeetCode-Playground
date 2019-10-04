class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        keys = sorted(counter.keys())
        ans = 0
        for i in range(1,len(keys)):
            if keys[i] -  keys[i-1] == 1:
                ans = max(ans,counter[keys[i]] + counter[keys[i-1]])
        return ans
        
            