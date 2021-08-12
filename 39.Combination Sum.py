class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import Counter
        dp = [[] for i in range(target+1)]
        for j in candidates:
            if j <= target:
                dp[j] = [[j]]

        for i in range(target):
            for j in candidates:
                if dp[i] and (i + j <= target):
                    temp = [x+[j] for x in dp[i]]
                    dp[i+j] = dp[i+j] + temp
        pre_ans = []
        for element in dp[-1]:
            temp = Counter(element)
            if temp not in pre_ans:
                pre_ans.append(temp)
        ans = []
        for i in pre_ans:
            temp = []
            for key, val in i.items():
                temp.extend([key]* val)
            ans.append(temp)
        return ans
