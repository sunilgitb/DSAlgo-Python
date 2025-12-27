from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Calculate the minimum time for all nodes to receive signal starting from node k.
        
        Args:
            times: List of [u, v, w] where u->v with weight w
            n: Total number of nodes (1 to n)
            k: Starting node
        
        Returns:
            Minimum time to reach all nodes, or -1 if some nodes are unreachable
        """
        # Build adjacency list
        adjacency_list = {i: [] for i in range(1, n + 1)}
        for source, target, weight in times:
            adjacency_list[source].append((target, weight))
        
        # Min-heap for Dijkstra: (total_time_from_k, node)
        min_heap = [(0, k)]
        
        # Track visited nodes and their minimum times
        visited = {}
        
        while min_heap:
            current_time, current_node = heapq.heappop(min_heap)
            
            # Skip if we already found a shorter path to this node
            if current_node in visited:
                continue
            
            # Record the shortest time to reach this node
            visited[current_node] = current_time
            
            # Explore neighbors
            for neighbor, travel_time in adjacency_list[current_node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (current_time + travel_time, neighbor))
        
        # Check if all nodes are reachable
        if len(visited) != n:
            return -1
        
        # Return the maximum time among all nodes (time for last node to receive signal)
        return max(visited.values())

# Example from the problem
print("Network Delay Time - Dijkstra's Algorithm:")
print("\nNetwork configuration:")
print("Number of nodes (n): 4")
print("Starting node (k): 2")
print("Transmission times:")
print("  2 → 1 (time 1)")
print("  2 → 3 (time 1)")
print("  3 → 4 (time 1)")

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

solution = Solution()
result = solution.networkDelayTime(times, n, k)

print(f"\nMinimum time for all nodes to receive signal: {result}")

print("\nExecution steps:")
print("1. Start from node 2 at time 0")
print("2. Node 2 can reach:")
print("   - Node 1: time 0 + 1 = 1")
print("   - Node 3: time 0 + 1 = 1")
print("3. Process node 1 (time 1):")
print("   - Node 1 has no outgoing edges")
print("4. Process node 3 (time 1):")
print("   - Node 3 → Node 4: time 1 + 1 = 2")
print("5. Process node 4 (time 2):")
print("   - Node 4 has no outgoing edges")
print("6. All nodes visited:")
print("   Node 1: time 1")
print("   Node 2: time 0")
print("   Node 3: time 1")
print("   Node 4: time 2")
print("Maximum time = 2")

print("\n" + "="*60)
print("Test Case 2: Some nodes unreachable")
print("\nNetwork configuration:")
print("Number of nodes (n): 3")
print("Starting node (k): 1")
print("Transmission times:")
print("  1 → 2 (time 1)")

times2 = [[1, 2, 1]]
n2 = 3
k2 = 1

result2 = solution.networkDelayTime(times2, n2, k2)
print(f"\nResult: {result2} (Node 3 is unreachable)")

print("\n" + "="*60)
print("Test Case 3: More complex network")
print("\nNetwork configuration:")
print("Number of nodes (n): 5")
print("Starting node (k): 1")
print("Transmission times:")
print("  1 → 2 (time 2)")
print("  1 → 3 (time 4)")
print("  2 → 3 (time 1)")
print("  2 → 4 (time 7)")
print("  3 → 5 (time 3)")
print("  4 → 5 (time 1)")

times3 = [[1, 2, 2], [1, 3, 4], [2, 3, 1], [2, 4, 7], [3, 5, 3], [4, 5, 1]]
n3 = 5
k3 = 1

result3 = solution.networkDelayTime(times3, n3, k3)
print(f"\nMinimum time for all nodes to receive signal: {result3}")

print("\nShortest paths from node 1:")
print("1 → 1: 0")
print("1 → 2: 2 (direct)")
print("1 → 3: min(4, 2+1=3) = 3 (via node 2)")
print("1 → 4: min(2+7=9, 3+? no direct) = 9 (via node 2)")
print("1 → 5: min(3+3=6, 9+1=10) = 6 (via nodes 1→2→3→5)")
print("Maximum time = 9")

print("\nComplexity Analysis:")
print("• Building adjacency list: O(E) where E = number of edges")
print("• Dijkstra with min-heap: O((V + E) log V)")
print("• Space complexity: O(V + E) for adjacency list + O(V) for heap")
print(f"• For this example: V={n3}, E={len(times3)}")
print(f"  Time: O(({n3} + {len(times3)}) log {n3}) ≈ O((5+6) log 5) ≈ O(11 * 2.32) ≈ O(25.5)")