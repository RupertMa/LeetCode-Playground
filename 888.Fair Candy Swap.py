class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B)) / 2
        setB = set(B)
        for a in A:
            if (a - diff) in setB: 
                return [a, int(a - diff)]
        