from typing import List

class Solution:
    def isNegativeWeightCycle(self, n: int, edges: List[List[int]]) -> int:
        """
        Using Bellman-Ford algorithm to detect negative weight cycles.
        Returns 1 if negative cycle exists, 0 otherwise.
        """
        # Step 1: Initialize distances from source to all vertices as INFINITE
        dist = [float('inf')] * n
        dist[0] = 0  # Assuming source is vertex 0
        
        # Step 2: Relax all edges |V| - 1 times
        for i in range(n - 1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        # Step 3: Check for negative-weight cycles
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return 1  # Negative cycle detected
        
        return 0  # No negative cycle

# Example
print("Detect Negative Weight Cycle using Bellman-Ford Algorithm:")
print("\nGraph 1: No negative cycle")
print("Number of vertices (n): 3")
print("Edges (u, v, weight):")
print("  0 → 1 (weight 2)")
print("  1 → 2 (weight 3)")
print("  0 → 2 (weight 6)")

edges1 = [[0, 1, 2], [1, 2, 3], [0, 2, 6]]
solution = Solution()
result1 = solution.isNegativeWeightCycle(3, edges1)

print(f"\nNegative cycle exists? {'Yes' if result1 == 1 else 'No'}")

print("\nBellman-Ford execution:")
print("Initial distances: [0, ∞, ∞]")
print("After 1st relaxation:")
print("  Edge 0→1: dist[1] = min(∞, 0+2) = 2")
print("  Edge 1→2: dist[2] = min(∞, 2+3) = 5")
print("  Edge 0→2: dist[2] = min(5, 0+6) = 5")
print("After 2nd relaxation (no changes)")
print("Final check: No edge can be relaxed further → No negative cycle")

print("\n" + "="*60)
print("\nGraph 2: Contains negative cycle")
print("Number of vertices (n): 4")
print("Edges (u, v, weight):")
print("  0 → 1 (weight 1)")
print("  1 → 2 (weight -1)")
print("  2 → 3 (weight -1)")
print("  3 → 1 (weight -1)")

edges2 = [[0, 1, 1], [1, 2, -1], [2, 3, -1], [3, 1, -1]]
result2 = solution.isNegativeWeightCycle(4, edges2)

print(f"\nNegative cycle exists? {'Yes' if result2 == 1 else 'No'}")

print("\nExplanation of negative cycle:")
print("Path: 1 → 2 → 3 → 1")
print("Total weight: (-1) + (-1) + (-1) = -3")
print("This creates a negative weight cycle that can be traversed infinitely")
print("to get arbitrarily small path weights")

print("\nBellman-Ford detection:")
print("After n-1 relaxations (3 in this case):")
print("  Distances approximate shortest paths")
print("In final check (nth relaxation):")
print("  Edge 3→1: dist[3] + (-1) < dist[1]")
print("  This additional relaxation possible → Negative cycle detected!")

print("\n" + "="*60)
print("\nGraph 3: Another example with negative edge but no negative cycle")
print("Number of vertices (n): 3")
print("Edges (u, v, weight):")
print("  0 → 1 (weight 5)")
print("  1 → 2 (weight -3)")
print("  2 → 0 (weight 2)")

edges3 = [[0, 1, 5], [1, 2, -3], [2, 0, 2]]
result3 = solution.isNegativeWeightCycle(3, edges3)

print(f"\nNegative cycle exists? {'Yes' if result3 == 1 else 'No'}")

print("\nExplanation:")
print("Cycle: 0 → 1 → 2 → 0")
print("Total weight: 5 + (-3) + 2 = 4 (positive)")
print("Has negative edge but no negative cycle")