# https://leetcode.com/problems/number-of-islands/

# DFS
from typing import List
import collections
import copy

# ---------------- DFS SOLUTION ----------------
class SolutionDFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        return res


# ---------------- BFS SOLUTION ----------------
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        res = 0

        def bfs(i, j):
            q = collections.deque([(i, j)])
            while q:
                r, c = q.popleft()
                if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                    continue
                grid[r][c] = '0'
                q.append((r - 1, c))
                q.append((r + 1, c))
                q.append((r, c - 1))
                q.append((r, c + 1))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i, j)

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            3
        ),
        (
            [
                ["1","1","1"],
                ["0","1","0"],
                ["1","1","1"]
            ],
            1
        ),
        (
            [
                ["0","0","0"],
                ["0","0","0"],
                ["0","0","0"]
            ],
            0
        )
    ]

    dfs_solver = SolutionDFS()
    bfs_solver = SolutionBFS()

    for idx, (grid, expected) in enumerate(test_cases, 1):
        print(f"Test Case {idx}")

        dfs_result = dfs_solver.numIslands(copy.deepcopy(grid))
        bfs_result = bfs_solver.numIslands(copy.deepcopy(grid))

        print(f"DFS Output: {dfs_result}")
        print(f"BFS Output: {bfs_result}")
        print(f"Expected : {expected}")
        print("-" * 40)

# Time for both dfs and bfs is = number of nodes + number of edges
# Time: O(n + e)
# Space: O(n) + o(n)  
# Auxiliary Space: O(n)