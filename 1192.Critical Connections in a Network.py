class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def make_graph(connnections):
            from collections import defaultdict
            graph = defaultdict(list)
            for edge in connections:
                a, b = edge
                graph[a].append(b)
                graph[b].append(a)
            return graph

        graph = make_graph(connections)
        ids = [0 for _ in range(n)]
        low_links = [0 for _ in range(n)]
        visited = [False for _ in range(n)]
        bridges = []

        node, prev_node, id = 0, -1, 0

        self.dfs(graph, node, prev_node, id, ids, low_links, visited, bridges)

        return bridges

    def dfs(self, graph, node, prev_node, id, ids, low_links, visited, bridges):
        ids[node] = id
        low_links[node] = id
        visited[node] = True
        id += 1

        for next_node in graph[node]:
            if next_node == prev_node:
                continue
            if not visited[next_node]:
                self.dfs(graph, next_node, node, id, ids, low_links, visited, bridges)
                low_links[node] = min(low_links[node], low_links[next_node])
                if ids[node] < low_links[next_node]:
                    bridges.append([node, next_node])
            else:
                low_links[node] = min(low_links[node], ids[next_node])

    # Leetcode hard is so hard! 
