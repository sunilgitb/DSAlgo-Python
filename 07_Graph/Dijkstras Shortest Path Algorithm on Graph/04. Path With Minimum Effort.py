from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        visited = set()
        minHeap = [(0, 0, 0)]  # (effort, row, col)
        
        while minHeap:
            effort, r, c = heapq.heappop(minHeap)
            
            if (r, c) == (row - 1, col - 1):
                return effort
                
            if (r, c) in visited:
                continue
                
            visited.add((r, c))
            
            # Explore all 4 directions
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < row and 0 <= nc < col:
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    heapq.heappush(minHeap, (new_effort, nr, nc))
        
        return 0

solution = Solution()

# Example 1
heights1 = [[1,2,2],[3,8,2],[5,3,5]]
print(solution.minimumEffortPath(heights1))  # Output: 2

# Example 2
heights2 = [[1,2,3],[3,8,4],[5,3,5]]
print(solution.minimumEffortPath(heights2))  # Output: 1

# Example 3
heights3 = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(solution.minimumEffortPath(heights3))  # Output: 0