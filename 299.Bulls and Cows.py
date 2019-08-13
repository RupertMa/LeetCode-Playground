class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        B = 0
        n = len(secret)
        unused = {}
        unseen = []
        for i in range(n):
            if guess[i] == secret[i]:
                A += 1
            else:
                unused[secret[i]] = unused.get(secret[i], 0) + 1
                unseen.append(i)
        for i in unseen:
            if (guess[i] in unused) and (unused[guess[i]]):
                B += 1
                unused[guess[i]] = unused[guess[i]] - 1
        return "{}A{}B".format(A,B)