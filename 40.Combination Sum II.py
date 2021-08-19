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
    #Time complexity: N = len(candidates) O(2*N)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import Counter
        from itertools import groupby
        count = Counter(candidates)
        count = [(num, count[num]) for num in count]
        ans = []
        self.dfs(ans, [], target, count, 0)
        return ans


    def dfs(self, ans, path, target, count, cur):
        if target == 0:
            ans.append(path[:])
            return None
        elif target < 0:
            return None
        for idx in range(cur, len(count)):
            num, freq = count[idx]
            if freq:
                count[idx] = (num, freq-1)
                path.append(num)
                self.dfs(ans, path, target-num, count, idx)
                path.pop()
                count[idx] = (num, freq)
        return None
    #Time complexity: N = len(candidates) O(2*N)
    # One important optimizaotio here is to use list and index instead of a dictionary.
    # So you won't regenerate the combinations.
    # counter like {1:3, 3:4, 5:2} target = 6
    # So you won't have [3,1,1,1] after you are done with all the combinations starting with 1 like [1,1,1,3]
