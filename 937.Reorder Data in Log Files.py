class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        for log in logs:
            if log.split(' ')[1].isnumeric():
                digit.append(log)
            else:
                letter.append(log.split(' ',1))
        letter = sorted(letter, key = lambda x:x[0])
        letter = sorted(letter, key = lambda x:x[1])
        letter = [" ".join(i) for i in letter]
        
        
        return letter + digit