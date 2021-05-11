class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        i = 0
        while i < min([len(j) for j in strs]):
            for prev_str, string in zip(strs, strs[1:]):
                if string[i] != prev_str[i]:
                    return ans
            ans += strs[0][i]
            i += 1
        return ans

    # Time complexity: O(M*N) N = len(strs), M = min([len(j) for j in strs])
