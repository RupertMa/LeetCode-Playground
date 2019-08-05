class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        import sys
        
        n = len(nums)
        r = 0
        ans = sys.maxsize
        Sum = 0
        for l in range(n):
            while r < n:
                Sum += nums[r]
                if Sum >= s:
                    if r - l + 1 < ans:
                        ans = r - l + 1
                    break
                r += 1
            Sum -= nums[l]
            if r <n:
                Sum -= nums[r]
        return ans if ans != sys.maxsize else 0

    def minSubArrayLen_Prime(self, s: int, nums: List[int]) -> int:
        import sys
        
        n = len(nums)
        r = 0
        ans = sys.maxsize
        Sum = 0
        for l in range(n):
            while r < n and Sum < s:
                Sum += nums[r]
                r += 1
            if Sum >= s and r - l < ans:
                ans = r - l
            Sum -= nums[l]
        
        return ans if ans != sys.maxsize else 0