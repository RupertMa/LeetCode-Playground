class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        import sys
        pa = sys.maxsize * -1
        pb = sys.maxsize * -1
        pc = sys.maxsize * -1
        na = sys.maxsize
        nb = sys.maxsize
        for num in nums:
            if num > pa:
                pa, pb, pc = num, pa, pb
            elif num > pb:
                pb, pc = num, pb
            elif num > pc:
                pc = num
            if num < na:
                na, nb = num, na
            elif num < nb:
                nb = num
        return max(na*nb*pa, pa*pb*pc)