class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1 and (not trust):
            return N
        pairs = {}
        truster=set()
        ppl = set([i for i in range(1,N+1)])
        for pair in trust:
            truster.add(pair[0])
            pairs[pair[1]] = pairs.get(pair[1],0) + 1
        judge = ppl - truster
        if len(judge) != 1:
            return -1
        j = judge.pop()
        
        if pairs[j] < N -1:
            return -1
        return j