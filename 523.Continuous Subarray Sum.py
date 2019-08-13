class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        dmap = {0:-1}
        Sum = 0
        for i,n in enumerate(nums):
            Sum += n
            m = Sum % k if k else Sum
            if m not in dmap: dmap[m] = i
            elif dmap[m] + 1 < i:
                return True
        return False