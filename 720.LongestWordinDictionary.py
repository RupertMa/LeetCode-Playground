class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wset = set([''])
        ans = ''
        #print(sorted(words))
        for word in sorted(words):
            if word[:-1] in wset:
                print(word[:-1])
                wset.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans
x=Solution()
print(x.longestWord(words=["w","wo","wor","worl", "world"]))