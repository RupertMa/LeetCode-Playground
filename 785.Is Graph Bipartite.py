from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import defaultdict
        edges = defaultdict(list)
        color = {}

        def dfs(p, c, edges):
            for vertex in edges[p]:
                if vertex not in color:
                    color[vertex] = not c
                    if not dfs(vertex, not c, edges):
                        return False
                else:
                    if color[vertex] == c:
                        return False

            return True
        for i, points in enumerate(graph):
            for p in points:
                edges[i].append(p)
        for p in edges:
            if p in color:
                continue
            color[p] = True
            if not dfs(p, True, edges):
                return False
        return True




x = Solution()
print(x.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
