class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        one = s.find('1')
        zero = s.find('0')
        ans = 0
        if one >= 0 and zero >= 0:
            pointer1 = ['0' if zero < one else '1', abs(one - zero)]
            pointer2 = ['1' if zero < one else '0', 1]
        else:
            return ans

        for c in s[max(one, zero)+1:]:
            if c== pointer2[0]:
                pointer2[1] += 1
            else:
                if min(pointer1[1], pointer2[1]) > 1:
                    ans += min(pointer1[1], pointer2[1])
                else:
                    ans += 1
                pointer1 = pointer2
                pointer2 = [c, 1]
        if pointer1[0] and pointer2[0]:
            if min(pointer1[1], pointer2[1]) > 1:
                ans += min(pointer1[1], pointer2[1])
            else:
                ans += 1
        return ans


        # Time complexity: O(N)
        # Space complexity: O(1)
