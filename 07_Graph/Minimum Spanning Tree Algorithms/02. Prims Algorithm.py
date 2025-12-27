import heapq

class Solution:
    def minCostConnectPoints(self, points):
        """
        Calculates the minimum cost to connect all points on a 2D plane.
        Cost between two points = Manhattan distance: |x1 - x2| + |y1 - y2|
        
        Args:
            points: List of [x, y] coordinates
        
        Returns:
            Minimum total cost to connect all points
        """
        n = len(points)
        
        # Build adjacency list
        adjList = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                # Undirected graph - add edges both ways
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        # Prim's Algorithm for MST
        visited = set()
        total_cost = 0
        minHeap = [(0, 0)]  # (distance, node) - start from node 0
        
        print("Prim's Algorithm Steps:")
        print("-" * 50)
        print(f"Starting from point 0 at ({points[0][0]}, {points[0][1]})")
        
        while len(visited) < n:
            dist, node = heapq.heappop(minHeap)
            
            if node in visited:
                print(f"  Node {node} already visited, skipping...")
                continue
                
            visited.add(node)
            total_cost += dist
            
            if dist > 0:  # Skip the initial 0 distance
                print(f"✓ Added connection to node {node} with cost {dist}")
                print(f"  Total cost so far: {total_cost}")
                print(f"  Visited nodes: {sorted(visited)}")
            
            # Add all neighbors of current node to min-heap
            for neighbor_dist, neighbor_node in adjList[node]:
                if neighbor_node not in visited:
                    heapq.heappush(minHeap, (neighbor_dist, neighbor_node))
        
        return total_cost


# Example usage
def run_example():
    print("=" * 50)
    print("PRIM'S ALGORITHM FOR MINIMUM SPANNING TREE")
    print("=" * 50)
    
    # Example 1: Simple 4 points
    points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print("\nExample 1: Points at positions:")
    for i, (x, y) in enumerate(points1):
        print(f"  Point {i}: ({x}, {y})")
    
    solution = Solution()
    result1 = solution.minCostConnectPoints(points1)
    print("\n" + "=" * 50)
    print(f"Minimum Cost to Connect All Points: {result1}")
    print("=" * 50)
    
    # Example 2: 3 points forming a triangle
    print("\n\nExample 2: Points at positions:")
    points2 = [[0, 0], [1, 1], [2, 0]]
    for i, (x, y) in enumerate(points2):
        print(f"  Point {i}: ({x}, {y})")
    
    result2 = solution.minCostConnectPoints(points2)
    print("\n" + "=" * 50)
    print(f"Minimum Cost to Connect All Points: {result2}")
    print("=" * 50)


if __name__ == "__main__":
    run_example()