from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        start, end = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                ans.append([start, end])
                start, end = intervals[i]
        ans.append([start, end])
        return ans

        # Time complexity: O(NlogN)
        # Space complexity: O(N)
