from typing import List

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        ans = 0
        if not S:
            return ans
        pointer1 = pointer2 = 0
        position = []
        while pointer2 < len(S):
            if S[pointer1] == S[pointer2]:
                pointer2 += 1
            else:
                position.append((S[pointer1], pointer2 - pointer1))
                pointer1 = pointer2
                pointer2 += 1
        position.append((S[pointer1], pointer2 - pointer1))

        for word in words:
            if self.stretchy(word, position[:]):
                ans += 1
        return ans

    def stretchy(self, word, position):
        pointer1 = 0
        pointer2 = 0
        while pointer2 < len(word):
            if word[pointer1] == word[pointer2]:
                pointer2 += 1
            else:
                if position:
                    c, c_length = position.pop(0)
                else:
                    return False
                length = pointer2 - pointer1
                if c!= word[pointer1] or (not ((length==c_length) or (length<=2 and c_length>=3) or (length>=3 and c_length>=length))):
                    return False
                pointer1 = pointer2
                pointer2 += 1

        if position:
            length = pointer2 - pointer1
            c, c_length = position.pop(0)
            if position or c!= word[pointer1] or (not ((length==c_length) or (length<=2 and c_length>=3) or (length>=3 and c_length>=length))):
                return False
            else:
                return True
        else:
            return False
