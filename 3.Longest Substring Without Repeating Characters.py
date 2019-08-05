class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        import sys
        
        n = len(s)
        ans = 0
        l = 0
        r = 0
        Set = set()
        for l in range(n):
            while r < n and s[r] not in Set:
                Set.add(s[r])
                r += 1
            if r-1 < n and s[r-1] in Set and r - l > ans:
                ans = r - l
            Set.remove(s[l])
        
        return ans
                