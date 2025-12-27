import heapq

class Solution:
    def minCostConnectPoints(self, points):
        """
        LeetCode 1584: Min Cost to Connect All Points
        Using Prim's Algorithm to find Minimum Spanning Tree
        """
        n = len(points)
        
        # Build adjacency list with Manhattan distances
        adjList = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                # Undirected graph: add edge both ways
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        # Prim's Algorithm
        visited = set()
        total_cost = 0
        minHeap = [(0, 0)]  # Start from point 0 with cost 0
        
        print("Building adjacency list...")
        for node, edges in adjList.items():
            print(f"  Point {node} ({points[node][0]},{points[node][1]}): ", end="")
            for dist, neighbor in edges:
                print(f"->{neighbor}({dist}) ", end="")
            print()
        print()
        
        print("Prim's Algorithm Execution:")
        print("-" * 60)
        
        while len(visited) < n:
            dist, node = heapq.heappop(minHeap)
            
            if node in visited:
                print(f"Pop: ({dist}, {node}) - Already visited, skipping")
                continue
                
            visited.add(node)
            total_cost += dist
            
            if dist > 0:  # Skip initial 0 cost
                print(f"✓ Added point {node} with cost {dist}")
                print(f"  Visited: {sorted(visited)} | Total cost: {total_cost}")
            
            # Add all unvisited neighbors to the heap
            for neighbor_dist, neighbor_node in adjList[node]:
                if neighbor_node not in visited:
                    heapq.heappush(minHeap, (neighbor_dist, neighbor_node))
        
        return total_cost


def run_example():
    print("=" * 60)
    print("LEETCODE 1584: MIN COST TO CONNECT ALL POINTS")
    print("=" * 60)
    
    # Test Case 1: From LeetCode example
    print("\nTest Case 1:")
    points1 = [[0,0], [2,2], [3,10], [5,2], [7,0]]
    print("Points: ", points1)
    
    solution = Solution()
    result1 = solution.minCostConnectPoints(points1)
    print("\n" + "-" * 60)
    print(f"RESULT: Minimum Cost = {result1}")
    print("-" * 60)
    
    # Test Case 2: Simple example
    print("\n\nTest Case 2:")
    points2 = [[0,0], [1,1], [2,0]]
    print("Points: ", points2)
    
    result2 = solution.minCostConnectPoints(points2)
    print("\n" + "-" * 60)
    print(f"RESULT: Minimum Cost = {result2}")
    print("-" * 60)
    
    # Test Case 3: 4 points forming a square
    print("\n\nTest Case 3:")
    points3 = [[0,0], [0,1], [1,0], [1,1]]
    print("Points: ", points3)
    
    result3 = solution.minCostConnectPoints(points3)
    print("\n" + "-" * 60)
    print(f"RESULT: Minimum Cost = {result3}")
    print("=" * 60)


if __name__ == "__main__":
    run_example()