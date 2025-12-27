# https://www.lintcode.com/problem/787
# https://leetcode.com/problems/the-maze/

from typing import List
import collections

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        q = collections.deque([start])

        while q:
            i, j = q.popleft()

            if maze[i][j] == 2:
                continue

            maze[i][j] = 2  # mark visited

            if [i, j] == destination:
                return True

            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                x, y = i, j

                # roll until hit wall
                while 0 <= x + dx < rows and 0 <= y + dy < cols and maze[x+dx][y+dy] != 1:
                    x += dx
                    y += dy

                if maze[x][y] == 0:
                    q.append([x, y])

        return False


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
    print(sol.hasPath(maze, start, destination))
    # Expected Output: True
