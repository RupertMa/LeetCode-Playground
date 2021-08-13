class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import Counter
        from itertools import groupby
        count = Counter(candidates)
        ans = []
        self.dfs(ans, [], target, count)
        return ans


    def dfs(self, ans, path, target, count):
        if target == 0:
            temp = sorted(path)
            if temp not in ans:
                ans.append(temp)
            return None
        elif target < 0:
            return None
        for key in count:
            if count[key]:
                temp = dict(count)
                temp[key] -= 1
                self.dfs(ans, path+[key], target-key, temp)
                count[key] -= 1
        return None
    #Time complexity: O(candidates * target)
