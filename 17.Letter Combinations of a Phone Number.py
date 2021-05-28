from typing import List

class Solution:
    def __init__(self):
        self.mapping = {'2':list('abc'), '3':list('def'), '4':list('ghi'), '5':list('jkl'),
                       '6':list('mno'), '7':list('pqrs'), '8':list('tuv'), '9':list('wxyz')}
    def letterCombinations(self, digits: str) -> List[str]:
        return ["".join(i) for i in self.helper(digits)]

    def helper(self, digits):
        if not digits:
            return []
        ans = []
        for letter in self.mapping[digits[0]]:
            combinations = self.helper(digits[1:])
            if combinations:
                for combination in combinations:
                    ans.append([letter] + combination)
            else:
                ans.append([letter])
        return ans

    # Time complexity: O(N^len(digits))
