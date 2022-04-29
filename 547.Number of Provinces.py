from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(set)
        for i in range(len(isConnected)):
            for j in range(i, len(isConnected[0])):
                if isConnected[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)
        ans = 0
        while graph:
            start = min(graph.keys())
            ans += 1
            queue = [start]
            while queue:
                cur = queue.pop(0)
                if cur in graph:
                    queue.extend(list(graph[cur]))
                    del graph[cur]
        return ans
