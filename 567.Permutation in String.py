class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length2=len(s2) ; length1 = len(s1)
        if length2 < length1:
            return False

        import string
        s_dic = {i:0 for i in string.ascii_lowercase}
        for i in s1:
            s_dic[i] += 1
        s_dic2 = {i:0 for i in string.ascii_lowercase}
        for i in range(length1):
            s_dic2[s2[i]] += 1
        if s_dic == s_dic2:
            return True
        for i in range(length1, length2):
            s_dic2[s2[i-length1]] -= 1
            s_dic2[s2[i]] += 1
            if s_dic == s_dic2:
                return True
        return False

        # Time complexity: O(N)
        # Space complexity: O(1)
