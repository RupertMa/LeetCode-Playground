class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if k == 0:
            return 0
        n = len(s)
        r = 0
        ans = dict()
        longest = 0 
        ansString = ""
        for l in range(n):
            while r < n and ((len(ans) < k) or (len(ans) ==k and s[r] in ans)):
                ans[s[r]] = ans.get(s[r], 0) + 1
                r += 1 

            if r-1 < n and len(ans) <= k and r - l > longest:
                longest = r - l
                ansString = s[l:r]
            ans[s[l]] -= 1 
            if ans[s[l]] == 0:
                del ans[s[l]]
        
        return longest
        