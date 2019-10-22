class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            emailSplit = email.split('@')
            temp = emailSplit[0].replace('.','')
            if '+' in temp:
                temp = temp[:temp.index('+')]
            emailSplit[0] = temp
            ans.add("@".join(emailSplit))
        return len(ans)