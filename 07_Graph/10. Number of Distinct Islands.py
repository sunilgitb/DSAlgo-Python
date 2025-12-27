# https://www.lintcode.com/problem/860
# https://leetcode.com/problems/number-of-distinct-islands/

from typing import List
import collections

class Solution:
    def numberof_distinct_islands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        row, col = len(grid), len(grid[0])
        uniqueIslands = set()

        def bfs(sr, sc):
            q = collections.deque()
            q.append((sr, sc))
            grid[sr][sc] = 0
            shape = []

            while q:
                r, c = q.popleft()
                shape.append((r - sr, c - sc))  # relative position

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))

            return tuple(shape)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    islandShape = bfs(i, j)
                    uniqueIslands.add(islandShape)

        return len(uniqueIslands)


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    grid = [
        [1,1,0,0,0],
        [1,0,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,0]
    ]

    sol = Solution()
    print(sol.numberof_distinct_islands(grid))
    # Expected Output: 1
