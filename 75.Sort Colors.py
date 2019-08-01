class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums) - 1)
    
    def quickSort(self, nums, l, r):
        if l < r:
            pivot = self.partition(nums, l, r)
            self.quickSort(nums, l, pivot-1)
            self.quickSort(nums, pivot+1, r)
            
        
    def partition(self, nums, l, r):
        left = l ; right = r
        pivot = nums[left]

        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left
        
        

