class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        visited[0] = 1
        queue = [0]
        while queue != []:
            s = queue.pop(0)
            for v in rooms[s]:
                if visited[v] == 0 and v != s:
                    visited[v] = 1
                    queue.append(v)
        print(visited)
        return visited == [1] * len(rooms)