class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        using = 0
        avoid = 0
        prev = None
        for num, count in sorted(counter.items()):
            if prev != num - 1:
                avoid, using = max(avoid, using), num * count + max(avoid, using)
            else:
                avoid, using = max(avoid, using), num * count + avoid
            prev = num
        return max(using, avoid)
