class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0
        Sum = 0
        preSum2 = {}
        for i in range(len(A)):
            Sum += A[i]
            ans += len(preSum2.get(Sum%K,[]))
            preSum2[Sum%K] = preSum2.get(Sum%K,[]) + [Sum]  
            if Sum % K == 0:
                ans += 1  
        return ans