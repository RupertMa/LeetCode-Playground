class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        k = len(nums) - k 
        
        pivot = self.partition(nums,l,r)
        
        while pivot != k:
            if pivot < k:
                l = pivot + 1
                pivot = self.partition(nums,l,r)
            elif pivot > k:
                r = pivot - 1
                pivot = self.partition(nums,l,r)
        return nums[k]
            
        
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