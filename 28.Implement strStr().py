class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m==0:
            return 0
        p1 = 0; p2 =0
        while p1 < n and p2<m:
            temp = p1
            while p1 < n and p2 < m:
                if haystack[p1] == needle[p2]:
                    if p2 == m-1:
                        return p1 - m + 1
                    p1+=1
                    p2+=1
                else:
                    p2 =0
                    p1 = temp + 1
                    break
        return -1
            