# https://www.lintcode.com/problem/663/
# Walls and Gates

from typing import List
import collections

class Solution:
    def walls_and_gates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return

        rows, cols = len(rooms), len(rooms[0])
        EMPTY = 2**31 - 1
        GATE = 0

        q = collections.deque()

        # Push all gates into queue (multi-source BFS)
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == GATE:
                    q.append((i, j))

        # BFS
        while q:
            i, j = q.popleft()
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols and rooms[x][y] == EMPTY:
                    rooms[x][y] = rooms[i][j] + 1
                    q.append((x, y))


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    INF = 2**31 - 1
    rooms = [
        [INF, -1,   0,  INF],
        [INF, INF, INF, -1 ],
        [INF, -1,  INF, -1 ],
        [0,   -1,  INF, INF]
    ]

    sol = Solution()
    sol.walls_and_gates(rooms)

    for row in rooms:
        print(row)
