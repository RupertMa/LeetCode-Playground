class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        l = []
        s = set([i for i in range(numCourses)])
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[1]].append(p[0])
            if p[0] in s:
                s.remove(p[0])
        while s:
            n = s.pop()
            l.append(n)
            edges = graph.get(n, [])[:]
            for m in edges:
                graph[n].remove(m)
                if m not in [j for i in graph.values() for j in i]:
                    s.add(m)
        if [j for i in graph.values() for j in i]:
            return False
        else:
            return True
