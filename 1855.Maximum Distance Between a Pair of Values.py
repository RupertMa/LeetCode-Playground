from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        length_1 = len(nums1)
        length_2 = len(nums2)
        ans = 0
        for i in range(min(length_1, length_2)):
            start = i + ans - 1
            for j in range(length_2-1, start, -1):
                if nums1[i] <= nums2[j]:
                    ans = max(ans, j-i)
                    break
        return ans
        # Time complexity: O(N**2)

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = p2 = ans = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                ans = max(ans, p2-p1)
                p2 += 1
            else:
                p1 += 1
        return ans
        # Time complexity: O(N)

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        length_1 = len(nums1)
        length_2 = len(nums2)
        last_i = 0
        ans = 0
        for j in range(length_2):
            for i in range(last_i, length_1):
                last_i = i
                if nums1[i] <= nums2[j]:
                    ans = max(ans, j-i)
                    break
        return ans
        # Time complexity: O(N)

        # nums2 is more important. ifs nums2[j] >= nums1[i], j++,
        # otherwise, i++
