class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = 0
        ans = ''
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        for i in range(1, len(num1)+1):
            num = ord(num1[-i]) + ord(num2[-i]) - 2 * ord('0') + res
            ans = str(num % 10) + ans
            res = num // 10
        i += 1
        while i <= len(num2):
            num = ord(num2[-i]) - ord('0') + res
            ans = str(num % 10) + ans
            res = num // 10
            i += 1
        if res:
            ans = str(res) + ans
        return ans

       # Time complexity: O(N)
       # Space complexity: O(1)
