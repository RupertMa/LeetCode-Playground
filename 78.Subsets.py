class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        subset = [] 
        results = []
        self.helper(results, subset, nums, 0)
        return results
    
    def helper(self, results, subset, nums, startIndex):
        results.append(subset[:])
        
        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.helper(results, subset, nums, i+1)
            subset.pop(-1)