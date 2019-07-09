class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word[1:].islower() or word.islower() or word.isupper()


#        import re
#        lst=re.findall('[a-z]+|[A-Z][a-z]+|[A-Z]+',word)
#        if lst[0]=word:
#        	return True
#        else:
#        	return False