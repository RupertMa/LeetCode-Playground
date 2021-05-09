class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_pop = population = 0
        year = None
        sweepLine = []
        for log in logs:
            sweepLine.append((True, log[0]))
            sweepLine.append((False, log[1]))
        sweepLine = sorted(sweepLine, key=lambda p: p[0])
        sweepLine = sorted(sweepLine, key=lambda p: p[1])
        for line in sweepLine:
            if line[0]:
                population += 1
            else:
                population -= 1
            if max_pop < population:
                max_pop = population
                year = line[1]
        return year
