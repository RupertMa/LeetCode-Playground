class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        ans = ''
        for x in range(len(set(s))):
            top, idx = s[0], 0
            counter = Counter(s)
            for y in range(len(s)):
                if top > s[y]:
                    top, idx = s[y], y
                if counter[s[y]] == 1:
                    break
                counter[s[y]] -= 1
            ans += top
            s = s[idx+1:].replace(top, '')
        return ans
