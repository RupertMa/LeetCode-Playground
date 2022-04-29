class Solution:
    def rotatedDigits(self, n: int) -> int:
        translate = {'2':'5', '5':'2', '6':'9', '9':'6'}
        ans = 0
        for i in range(1, n+1):
            chars = str(i)
            if ('3' in chars) or ('4' in chars) or ('7' in chars):
                continue
            rotated_chars = ''
            for s in chars:
                rotated_chars += translate[s] if s in translate else s
            if int(rotated_chars) != i:
                ans += 1
        return ans
    # Time complexity: O(N * len(N))
