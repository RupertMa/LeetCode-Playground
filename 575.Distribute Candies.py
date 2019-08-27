class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        assert len(candies) % 2 == 0
        kinds = len(set(candies))
        return min(kinds, len(candies)//2)
                
            
        