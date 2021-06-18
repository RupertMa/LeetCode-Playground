class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0}
        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                change[5] -= 1
                change[10] += 1
            elif bill == 20:
                if change[10] > 0:
                    change[10] -= 1
                    change[5] -= 1
                else:
                    change[5] -= 3
            if (change[5] < 0) or (change[10] < 0):
                return False
        return True

    # Time complexity: O(N)
