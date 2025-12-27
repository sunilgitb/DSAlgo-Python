# https://leetcode.com/problems/trapping-rain-water-ii/
# https://youtu.be/QvQiQcLCQ4Y

import heapq
class Solution:
    def trapRainWater(self, heightMap):
        minHeap = []
        ROW, COL = len(heightMap), len(heightMap[0])
        visited = [[False]*COL for _ in range(ROW)]
        
        for i in range(ROW):
            for j in range(COL):
                if i in (0, ROW-1) or j in (0, COL-1):
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        res = 0
        minBdH = 0  # Minimum Boundary Height
        while minHeap:
            h, i, j = heapq.heappop(minHeap)
            minBdH = max(minBdH, h)
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                r, c = i+dx, j+dy
                if 0<=r<ROW and 0<=c<COL and not visited[r][c]:
                    visited[r][c] = True
                    heapq.heappush(minHeap, (heightMap[r][c], r, c))
                    if heightMap[r][c] < minBdH:
                        res += minBdH - heightMap[r][c]
        
        return res
    
    
    
# Time: O(m*n * log(m*n))
# Space: O(m*n)
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    heightMap = [
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
    ]
    print("Trapped Water:", sol.trapRainWater(heightMap))
    # Expected Output: 4

    # Test Case 2
    heightMap = [
        [3,3,3,3,3],
        [3,2,2,2,3],
        [3,2,1,2,3],
        [3,2,2,2,3],
        [3,3,3,3,3]
    ]
    print("Trapped Water:", sol.trapRainWater(heightMap))
    # Expected Output: 10

    # Test Case 3
    heightMap = [
        [1,1,1,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,1,1,1]
    ]
    print("Trapped Water:", sol.trapRainWater(heightMap))
    # Expected Output: 4
