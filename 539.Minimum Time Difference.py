class Solution:
    import sys
    def calDifference(self,time1,time2):
        diff = abs((time1[0]-time2[0])*60 + (time1[1]-time2[1]))
        if diff > 12*60:
            diff = 24*60 - diff
        return diff
        
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePart = []
        for time in timePoints:
             timePart.append(list(map(int, time.split(":"))))
        timePart = sorted(timePart, key = lambda x: x[1])
        timePart = sorted(timePart, key = lambda x: x[0])
        ans = sys.maxsize
        for i in range(1,len(timePoints)):
            ans = min(ans,self.calDifference(timePart[i],timePart[i-1]))
        ans = min(ans,self.calDifference(timePart[0],timePart[-1]))
        return ans