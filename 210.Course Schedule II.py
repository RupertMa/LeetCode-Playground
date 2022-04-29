class Solution:
    def __init__(self):
        self.l = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        global temp
        global permanent
        global unmarked

        unmarked = set([i for i in range(numCourses)])
        permanent = set()
        temp = set()

        while len(permanent) != numCourses:
            n = unmarked.pop()
            if not self.visit(n, graph):
                return []
        return self.l

    def visit(self, n, graph):
        if n in permanent:
            return True
        if n in temp:
            return False

        temp.add(n)
        for m in graph[n]:
            if not self.visit(m, graph):
                return False
        temp.remove(n)
        unmarked.discard(n)
        permanent.add(n)
        self.l = [n] + self.l
        return True

# Time complexity: O(N)
# Space complexity: O(N)
