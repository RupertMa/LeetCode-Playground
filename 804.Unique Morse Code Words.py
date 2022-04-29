class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        import string
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        translate = dict(zip(list(string.ascii_lowercase), morse))
        ans = set()
        for word in words:
            temp = ''
            for s in word:
                temp += translate[s]
            ans.add(temp)
        return len(ans)

        #Time complexity: O(N)
        #Space complexity: O(M) depends on the variety of unique Morse words
