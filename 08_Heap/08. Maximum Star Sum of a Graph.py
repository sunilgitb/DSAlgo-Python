# https://leetcode.com/problems/maximum-star-sum-of-a-graph/

import heapq
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adjList = {i:[] for i in range(len(vals))}
        
        for a, b in edges:
            if vals[b] > 0: 
                heapq.heappush(adjList[a], vals[b])
                if len(adjList[a]) > k:
                    heapq.heappop(adjList[a])
            if vals[a] > 0:
                heapq.heappush(adjList[b], vals[a])
                if len(adjList[b]) > k:
                    heapq.heappop(adjList[b])
                    
        res = -2**31
        for i in range(len(vals)):
            tmp = vals[i]
            tmp += sum(adjList[i])
            res = max(res, tmp)
            
        return res
    
    
# Time: O(N + E * log(K))
# Space: O(N*K)
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    vals = [1, 2, 3, 4, 10, -10, -20]
    edges = [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5]]
    k = 2
    print("Maximum Star Sum:", sol.maxStarSum(vals, edges, k))
    # Explanation: Center at node 4: 10 + 4 + 3 = 17

    # Test Case 2
    vals = [-1, -2, -3, -4]
    edges = [[0, 1], [1, 2], [2, 3]]
    k = 2
    print("Maximum Star Sum:", sol.maxStarSum(vals, edges, k))
    # Expected: -1 (only choose a single node with max value)

    # Test Case 3
    vals = [5, 2, 1, 8, 6]
    edges = [[0, 1], [0, 2], [0, 3], [3, 4]]
    k = 2
    print("Maximum Star Sum:", sol.maxStarSum(vals, edges, k))
    # Expected: 5 + 8 + 6 = 19 (center at node 3 with 2 neighbors)
