class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Time complexity: O(klogk)
        # Space complexity: O(k)
        from heapq import heappush, heappop

        visited = set()
        heap = []
        ans = []
        len_1 = len(nums1)
        len_2 = len(nums2)
        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0,0))
        while len(ans) < k and heap:
            cur = heappop(heap)
            if cur[1] + 1 < len_1 and (cur[1] + 1, cur[2]) not in visited:
                heappush(heap, (nums1[cur[1]+1] + nums2[cur[2]], cur[1]+1, cur[2]))
                visited.add((cur[1]+1, cur[2]))
            if cur[2] + 1 < len_2 and (cur[1], cur[2] + 1) not in visited:
                heappush(heap, (nums1[cur[1]] + nums2[cur[2]+1], cur[1], cur[2]+1))
                visited.add((cur[1], cur[2]+1))
            ans.append((nums1[cur[1]], nums2[cur[2]]))

        return ans
