ransomNote='aacc'
magazine='aabccdsdq'
ransomNote=list(ransomNote)
magazine=list(magazine)
l=list()
for letter in ransomNote:
    if letter in magazine: 
    	l.append(letter)
    	magazine.remove(letter)
if ransomNote == l: print True
else: print False
