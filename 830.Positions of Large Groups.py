class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        pointer = 0
        curS = ''
        ans = []
        for i,s in enumerate(S):
            if s != curS:
                curS = s
                if i - pointer >= 3:
                    ans.append([pointer,i-1])
                pointer = i
        if curS == S[-1] and len(S) - pointer >=3:
            ans.append([pointer, i])
        return ans