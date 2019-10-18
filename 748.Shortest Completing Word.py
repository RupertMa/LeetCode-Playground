class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counter = {}
        for s in licensePlate:
            if s.isalpha():
                counter[s.lower()] = counter.get(s.lower(),0) + 1
        ans = "1" * (max(map(len,words)) + 1)
        for word in sorted(words, key=lambda x: len(x)):
            cond = True
            for key in counter.keys():
                if word.count(key) < counter[key]:
                    cond = False
                    break
            if cond and len(word) < len(ans):
                return word