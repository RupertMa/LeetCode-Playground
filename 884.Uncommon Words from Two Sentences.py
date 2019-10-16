class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter
        count = Counter(A.split(" ")+B.split(" "))
        return [k for k,v in count.items() if v==1]