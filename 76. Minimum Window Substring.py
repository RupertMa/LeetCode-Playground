class Solution:
    def largerDict(self, d1:dict, d2:dict) -> bool:
        if d1.keys() != d2.keys():
            return False
        for key in d1.keys():
            if d1[key] < d2[key]:
                return False
        return True
        
    def minWindow(self, s: str, t: str) -> str:
        import sys
        
        T = dict()
        for i in t:
            T[i] = T.get(i,0) + 1
        n = len(s)
        for i in range(n):
            if s[i] in T:
                r = i
                start = i
                break
        subString = dict()
        ans = sys.maxsize
        ansString = ""
        for l in range(n):
            if s[l] in T:
                while r < n and (not self.largerDict(subString,T)):
                    if s[r] in T:
                        subString[s[r]] = subString.get(s[r],0) + 1
                    r += 1
                if r-1 < n and self.largerDict(subString,T) and r - l < ans:
                    ans = r - l
                    ansString = s[l:r]
                subString[s[l]] -= 1
        return ansString