# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/


# Method 1: Floyd Warshall Algorithm (Dynamic Programming)

class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        dist = [[float('inf')] * n for _ in range(n)]

        # Initialize distances
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd–Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        dist[i][j] = 0
                    else:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        min_reach = n
        res = 0

        for i in range(n):
            reachable = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    reachable += 1

            # If tie, choose city with larger index
            if reachable <= min_reach:
                min_reach = reachable
                res = i

        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    solver = Solution()

    # Test Case 1
    n = 4
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    distanceThreshold = 4
    print("Output:", solver.findTheCity(n, edges, distanceThreshold))
    print("Expected: 3")
    print("-" * 40)

    # Test Case 2
    n = 5
    edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
    distanceThreshold = 2
    print("Output:", solver.findTheCity(n, edges, distanceThreshold))
    print("Expected: 0")
 
# Time: O(N^3)
# Space: O(N^2)




# Method 2: Dijkstra's Algorithm
'''
we can use Dijkstra's Shortest Path Algorithm for each node to find sortest path to each node. 
But time complexity would be O(N^3 log(N)) for using that minHeap
'''