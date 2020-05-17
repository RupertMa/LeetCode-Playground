class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        for i in range(n-1):
            a, b = words[i], words[i+1]
            Min = min(len(a),len(b))
            if a[:Min] == b[:Min] and len(a) > len(b):
                return False
            for j in range(Min):
                if order.index(a[j]) < order.index(b[j]):
                    break
                elif order.index(a[j]) == order.index(b[j]):
                    continue
                else: 
                    return False
        return True