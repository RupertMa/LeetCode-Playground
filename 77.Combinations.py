class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(range(1, n+1), k, [], ans)
        return ans

    def dfs(self, nums, k, path, ans):
        if len(path) == k:
            ans.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k, path+[nums[i]], ans)
    #Time complexity: O(k * n)
