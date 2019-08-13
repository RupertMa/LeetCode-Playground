class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        dmap = {0:[-1]} 
        Sum = 0
        for i,n in enumerate(nums):
            Sum += n
            m = Sum - k
            if m in dmap:
                ans += len(dmap[m])
            dmap[Sum] = dmap.get(Sum,[]) + [i]
        return ans