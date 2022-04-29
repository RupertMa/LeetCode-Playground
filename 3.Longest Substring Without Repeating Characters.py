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

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        p1 = p2 = 0
        ans = 0
        while p2 < len(s):
            if s[p2] not in seen:
                seen.append(s[p2])
            else:
                ans = max(ans, len(seen))
                pos = seen.index(s[p2])
                p1 = pos + 1
                seen = seen[p1:]
                seen.append(s[p2])
            p2 += 1
        return max(ans, len(seen))

    # Time complexity: O(N)
    # Space complexity: O(N)
