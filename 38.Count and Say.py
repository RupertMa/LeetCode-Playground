class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(n-1):
            ans = self.readOff(ans)
        return ans
    
    def readOff(self,n):
        p = 0
        output = ""
        count = 0
        while p < len(n): 
            if p<len(n)-1 and n[p] == n[p+1]:
                count += 1
                p += 1
            else:
                count += 1
                output = output + str(count) +n[p] 
                count = 0
                p += 1
        return output
        