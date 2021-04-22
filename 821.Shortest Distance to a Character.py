class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        left = s.find(c)
        ans = [i for i in range(left,-1,-1)] + [10**4+1] * (len(s) - left - 1)
        for i in range(left+1, len(s)):
            if s[i] != c:
                ans[i] = min(abs(i-left), ans[i])
            else:
                ans[i] = 0
                for j in range(int(round((left + i)/2,0)), i):
                    ans[j] = min(abs(i - j), ans[j])
                left = i
        return ans

        # Space complexity: O(N)
        # Time complexity:O(N) ~ O(N**2)

    # Method 2:
    # Easier to understand
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        prev = len(s)
        for i in range(len(s)):
            if s[i] == c:
                prev = i
            ans.append(abs(prev - i))
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], abs(prev - i))
        return ans
        # Space complexity: O(N)
        # Time complexity:O(N)
