from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x==1 and y==1:
            return [2] if bound>=2 else []
        ans = set()
        power = 0
        Sum = 2

        while Sum <= bound:
            ans.add(Sum)
            extra=1
            old_sum = Sum
            while y > 1 and Sum <= bound:
                Sum = x**power + y**(power+extra)
                if Sum <= bound:
                    ans.add(Sum)
                extra += 1
            extra = 1
            Sum = old_sum
            while x > 1 and Sum <= bound:
                Sum = x**(power+extra) + y**power
                if Sum <= bound:
                    ans.add(Sum)
                extra += 1
            power += 1
            Sum = x**power + y**power

        return list(ans)

        # Time complexity: Let N = log_x(bound) and M = log_y(bound) then O(N*M)
        # Space complexity: O(N*M) depends on the # of unique power integers
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        a = bound if x == 1 else int(log(bound, x))
        b = bound if y == 1 else int(log(bound, y))

        powerful_integers = set([])

        for i in range(a + 1):
            for j in range(b + 1):

                value = x**i + y**j

                if value <= bound:
                    powerful_integers.add(value)

                if y == 1:
                    break

            if x == 1:
                break

        return list(powerful_integers)
