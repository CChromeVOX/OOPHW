from collections import deque
import unittest

def bfs(graph, start, process_node):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        process_node(node)  

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

class BFSTestCase(unittest.TestCase):
    def test_small_graph_one_connected_component(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }
        expected_output = ['A', 'B', 'C', 'D', 'E', 'F']
        result = []
        bfs(graph, 'A', result.append)
        self.assertEqual(result, expected_output)

    def test_disconnected_graph_multiple_connected_components(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B'],
            'F': ['C']
        }
        expected_output = ['A', 'B', 'C', 'D', 'E', 'F']
        result = []
        bfs(graph, 'A', result.append)
        self.assertEqual(result, expected_output)

    def test_graph_no_edges(self):
        graph = {
            'A': [],
            'B': [],
            'C': [],
            'D': [],
            'E': []
        }
        expected_output = ['A']
        result = []
        bfs(graph, 'A', result.append)
        self.assertEqual(result, expected_output)

    def test_graph_multiple_connected_components(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['A'],
            'C': ['A'],
            'D': ['E'],
            'E': ['D']
        }
        expected_output = ['A', 'B', 'C']
        result = []
        bfs(graph, 'A', result.append)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
