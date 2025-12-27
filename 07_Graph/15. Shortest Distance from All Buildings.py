# https://www.lintcode.com/problem/803/

from typing import List
from collections import deque

class Solution:
    def shortest_distance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        total_buildings = 0
        reach_count = [[0] * n for _ in range(m)]
        distance_sum = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_buildings += 1
                    queue = deque([(i, j)])
                    visited = set([(i, j)])
                    level_distance = 0
                    
                    while queue:
                        level_distance += 1
                        for _ in range(len(queue)):
                            r, c = queue.popleft()
                            for dr, dc in ((0,1), (0,-1), (1,0), (-1,0)):
                                x, y = r + dr, c + dc
                                if (
                                    0 <= x < m and 0 <= y < n and
                                    grid[x][y] == 0 and
                                    (x, y) not in visited
                                ):
                                    visited.add((x, y))
                                    reach_count[x][y] += 1
                                    distance_sum[x][y] += level_distance
                                    queue.append((x, y))
        
        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach_count[i][j] == total_buildings:
                    ans = min(ans, distance_sum[i][j])
        
        return -1 if ans == float('inf') else ans


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    grid = [
        [1, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]

    sol = Solution()
    print(sol.shortest_distance(grid))
