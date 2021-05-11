from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            temp = self.twoSum(nums[:i] + nums[i+1:], -nums[i])
            if temp:
                for j in temp:
                    ans.add(tuple(sorted([nums[i]] + j)))
        return [list(i) for i in ans]

    def twoSum(self, nums, target):
        seen = set()
        ans = []
        for num in nums:
            if target - num not in seen:
                seen.add(num)
            else:
                ans.append([num, target-num])
        return ans

x = Solution()
print(x.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
