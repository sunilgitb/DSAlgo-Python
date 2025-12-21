# https://leetcode.com/problems/min-cost-to-connect-all-points/
# https://youtu.be/f7JOBJIC-NA
# Minimum Spanning Tree (MST)

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))

        visited = set()
        res = 0
        minHeap = [(0, 0)]  # (cost, node)

        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res += cost

            for edge in adjList[node]:
                if edge[1] not in visited:
                    heapq.heappush(minHeap, edge)

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    # Expected Output: 20

    sol = Solution()
    result = sol.minCostConnectPoints(points)
    print("Minimum Cost to Connect All Points:", result)



# V = number of umber of verices and E = numver of Edges in the graph.
# Time: O(V^2) + O((V+E)logV) = O(V^2)
# Space: O(V^2)  In worst cases all connections of undirected graph can be in minheap 