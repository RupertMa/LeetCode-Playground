from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        left = 0
        right = len(nums) - 1
        find_left = find_right = False
        if not nums or nums[left] > target or nums[right] < target:
                return ans
        while left <= right and ((not find_left) or (not find_right)):
            if nums[left] == target:
                ans[0] = left
                find_left = True
            if nums[right] == target:
                ans[1] = right
                find_right = True
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if nums[left] < target:
                    left += 1
                elif nums[right] > target:
                    right -= 1
            #print(left, right, find_left, find_right)
        return ans

x = Solution()
print(x.searchRange(nums = [5,7,7,8,8,10], target = 8))

print(x.searchRange(nums = [5,7,7,8,8,8,10], target = 8))

print(x.searchRange(nums = [5,7,7,8,8,8,9,10], target = 8))

print(x.searchRange(nums = [5,7,7,8,8,8,9,10], target = 9))
