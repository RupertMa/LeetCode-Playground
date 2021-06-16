class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)
        for i in range(0, size):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1]!= 1) and (i == size -1 or flowerbed[i+1] != 1):
                count += 1
                flowerbed[i] = 1
            if count >= n:
                return True
        return count >= n
    # Time complexity: O(N)
