class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        counter = {}
        for line in wall:
            cum = 0
            for length in line[:-1]:
                cum += length
                counter[cum] = counter.get(cum, 0) + 1
        return n - max(counter.values()) if counter else n

        # Time complexity: O(N) (N: # of elements in wall)
        # Space complexity: O(N)
