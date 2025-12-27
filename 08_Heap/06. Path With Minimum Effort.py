from typing import List
import collections

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        
        def canReach(maxEffort: int) -> bool:
            visited = [[False]*col for _ in range(row)]
            q = collections.deque([(0, 0)])
            visited[0][0] = True
            
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            
            while q:
                r, c = q.popleft()
                if r == row-1 and c == col-1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
                        if abs(heights[r][c] - heights[nr][nc]) <= maxEffort:
                            visited[nr][nc] = True
                            q.append((nr, nc))
            return False
        
        # Binary Search
        low, high = 0, 10**6
        answer = high
        while low <= high:
            mid = (low + high) // 2
            if canReach(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return answer


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()
    
    heights1 = [[1,2,2],[3,8,2],[5,3,5]]
    print("Minimum Effort Path 1:", sol.minimumEffortPath(heights1))  # Output: 2

    heights2 = [[1,2,3],[3,8,4],[5,3,5]]
    print("Minimum Effort Path 2:", sol.minimumEffortPath(heights2))  # Output: 1

    heights3 = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    print("Minimum Effort Path 3:", sol.minimumEffortPath(heights3))  # Output: 0
