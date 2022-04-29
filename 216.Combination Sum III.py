class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1,10)]
        ans = []
        self.dfs(candidates, n, k, ans, [], 0)
        return ans

    def dfs(self, candidates, n, k, ans, path, cur):
        if n == 0 and len(path) ==k:
            ans.append(path)
            return None

        for idx in range(cur, len(candidates)):
            pick = candidates[idx]
            if n - pick < 0:
                break

            self.dfs(candidates, n-pick, k, ans, path+[candidates[idx]], idx+1)
    #Time complexity: O(2**N) where N=9
    #Space complexity: O(k)
