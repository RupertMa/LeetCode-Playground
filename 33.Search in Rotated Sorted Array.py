class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            median = (l + r) // 2
            if nums[median] == target:
                return median
            if nums[median] >= nums[l]:
                if target < nums[median] and target >= nums[l]:
                    r = median
                else:
                    l = median + 1

            else:
                if nums[median] < target and target <= nums[r]:
                    l = median
                else:
                    r = median - 1
                
        if nums and nums[l] == target:
            return l
        
        return -1
            