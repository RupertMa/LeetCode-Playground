class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sweepLine = []
        for trip in trips:
            sweepLine.append((True, trip[1], trip[0]))
            sweepLine.append((False, trip[2], trip[0]))
        sweepLine = sorted(sweepLine, key=lambda triple:triple[0])
        sweepLine = sorted(sweepLine, key=lambda triple:triple[1])
        
        numPassengers = 0
        for line in sweepLine:
            if line[0]==True: 
                numPassengers += line[2]
            else:
                numPassengers -= line[2]        
            if numPassengers > capacity:
                return False
        return True