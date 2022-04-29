from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

        # Time complexity: O(NMlog(M)) N = len(strs), M = max(len(s) for s in str)
        # Space complexity: O(N)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for i in s:
                key[ord(i)-ord('a')] += 1
            ans[tuple(key)].append(s)
        return ans.values()
        # Time complexity: O(NM) N = len(strs), M = max(len(s) for s in str)
        # Space complexity: O(N)
