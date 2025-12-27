# https://www.lintcode.com/problem/788/
# https://leetcode.com/problems/the-maze-ii/

from typing import List
import collections

class Solution:
    def shortest_distance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        
        # Distance matrix
        distance = [[float('inf')] * cols for _ in range(rows)]
        distance[start[0]][start[1]] = 0

        q = collections.deque()
        q.append((start[0], start[1]))

        while q:
            i, j = q.popleft()

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                x, y = i, j
                d = distance[i][j]

                # roll until hit wall
                while 0 <= x + dx < rows and 0 <= y + dy < cols and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    d += 1

                # relax distance
                if d < distance[x][y]:
                    distance[x][y] = d
                    q.append((x, y))

        res = distance[destination[0]][destination[1]]
        return res if res != float('inf') else -1


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    maze = [
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]
    ]

    start = [0, 4]
    destination = [4, 4]

    sol = Solution()
    print(sol.shortest_distance(maze, start, destination))
    # Expected Output: 12
