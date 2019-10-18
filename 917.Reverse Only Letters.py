class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        pointer1 = 0
        pointer2 = len(S) - 1
        while pointer1 < pointer2:
            while (pointer1 < pointer2) and (not S[pointer1].isalpha()):
                pointer1 += 1
            while (pointer1 < pointer2) and not S[pointer2].isalpha():
                pointer2 -= 1
            if pointer1 < pointer2:
                S[pointer1], S[pointer2] = S[pointer2], S[pointer1]
                pointer1 += 1
                pointer2 -= 1
        return "".join(S)
