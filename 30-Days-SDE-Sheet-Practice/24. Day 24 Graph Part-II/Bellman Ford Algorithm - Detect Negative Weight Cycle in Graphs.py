# https://practice.geeksforgeeks.org/problems/negative-weight-cycle3504/1#
# https://youtu.be/75yC1vbS8S8

# Method 1: Bellman Ford Algorithm
class SolutionBellmanFord:
    def isNegativeWeightCycle(self, n, edges):
        INF = 2**31
        dist = [INF] * n
        dist[0] = 0

        # Relax edges n-1 times
        for _ in range(n - 1):
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # One more relaxation to detect negative cycle
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return 1  # Negative cycle exists

        return 0


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    test_cases = [
        # (n, edges, expected)
        (3, [[0,1,-1],[1,2,-2],[2,0,-3]], 1),   # Negative cycle
        (3, [[0,1,4],[1,2,3]], 0),              # No cycle
        (4, [[0,1,1],[1,2,-1],[2,3,-1],[3,1,-1]], 1)
    ]

    solver = SolutionBellmanFord()

    for i, (n, edges, expected) in enumerate(test_cases, 1):
        print(f"Test Case {i}")
        print("Output  :", solver.isNegativeWeightCycle(n, edges))
        print("Expected:", expected)
        print("-" * 40)


		
# Time: O(V * E)
# Space: O(V)
# Where V = number of vertices and E = number of edges



''' 
# Method 2: Dijkstra's Shortest Path Algorithm

class Solution:
    def isNegativeWeightCycle(self, n, edges):
        #Code here
        adjList = {i:[] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append((edge[2], edge[1])) # (weight. node)
            
        for i in range(n):
            visited = [False] * n
            minHeap = [(0, i)]
            while minHeap:
                dist, node = heapq.heappop(minHeap)
                if visited[node] == True: 
                    if node == i and dist < 0: return 1
                    continue
                visited[node] = True
                for c in adjList[node]:
                    heapq.heappush(minHeap, (dist + c[0], c[1]))
        
        return 0

# Time: O(N * E * log(E))
# Space: O(N * E)
'''