from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges_numb = len(connections)
        graph = {k: [] for k in range(n)}
        for c in connections:
            nodes_1 = graph[c[0]]
            nodes_2 = graph[c[1]]
            nodes_1.append(c[1])
            nodes_2.append(c[0])
            graph[c[0]] = nodes_1
            graph[c[1]] = nodes_2
        comp_numb = 0
        visited = [0] * len(graph)
        for k in graph:
            if visited[k] == 0:
                comp_numb += 1
                dfs(graph, k, visited)
        if edges_numb < n - 1:
            return -1
        else:
            return comp_numb - 1

def dfs(graph, s, visited):
    visited[s] = 1
    for v in graph[s]:
        if visited[v] == 0:
            dfs(graph, v, visited)