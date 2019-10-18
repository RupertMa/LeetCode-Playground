class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fastPointer = slowPointer = 0
        while fastPointer < len(nums):
            if nums[fastPointer] != nums[slowPointer]:
                slowPointer += 1
                nums[slowPointer] = nums[fastPointer]
            fastPointer += 1
        return slowPointer+1
        