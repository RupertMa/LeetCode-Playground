# Kahn's algorithm

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


# DFS
class Solution:
    def __init__(self):
        self.l = []

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        global edges
        global unmarked
        global temp
        global permanent

        from collections import defaultdict
        edges = defaultdict(list)
        for (a, b) in prerequisites:
            edges[b].append(a)


        unmarked = set([i for i in range(numCourses)])
        temp = set()
        permanent = set()
        while len(permanent) != numCourses:
            n = unmarked.pop()
            if not self.visit(n):
                return False
        return True

    def visit(self, n):
        if n in permanent:
            return True
        if n in temp:
            print('should be here')
            return False

        temp.add(n)
        for m in edges[n]:
            if not self.visit(m):
                return False
        temp.remove(n)
        unmarked.discard(n)
        permanent.add(n)
        self.l = [n] + self.l
        return True
