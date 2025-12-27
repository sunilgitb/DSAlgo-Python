from typing import List
import heapq
import math

class SmallestNeighborsAtThreshold:
    """
    Problem: Find city with smallest number of reachable cities within distance threshold
             If multiple cities have same count, return city with greatest value
    """
    
    # Method 1: Floyd Warshall Algorithm (All-pairs shortest path)
    def findTheCityFloydWarshall(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Set diagonal to 0 (distance to itself)
        for i in range(n):
            dist[i][i] = 0
        
        # Add edges (undirected graph)
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd Warshall algorithm
        for k in range(n):
            for i in range(n):
                # Optimization: Skip if dist[i][k] is infinity
                if dist[i][k] == float('inf'):
                    continue
                for j in range(n):
                    # Update if path through k is shorter
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find city with smallest number of reachable cities
        min_reachable = n
        result_city = 0
        
        for city in range(n):
            reachable_count = 0
            for neighbor in range(n):
                if city != neighbor and dist[city][neighbor] <= distanceThreshold:
                    reachable_count += 1
            
            # Update result based on conditions
            if reachable_count < min_reachable:
                min_reachable = reachable_count
                result_city = city
            elif reachable_count == min_reachable and city > result_city:
                result_city = city
        
        return result_city
    
    # Method 2: Dijkstra's Algorithm from each node
    def findTheCityDijkstra(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        min_reachable = n
        result_city = 0
        
        # Run Dijkstra from each city
        for city in range(n):
            # Dijkstra's algorithm
            distances = [float('inf')] * n
            distances[city] = 0
            heap = [(0, city)]  # (distance, node)
            
            while heap:
                curr_dist, node = heapq.heappop(heap)
                
                # Skip if we found a better distance already
                if curr_dist > distances[node]:
                    continue
                
                # Explore neighbors
                for neighbor, weight in graph[node]:
                    new_dist = curr_dist + weight
                    
                    if new_dist < distances[neighbor] and new_dist <= distanceThreshold:
                        distances[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))
            
            # Count reachable cities (excluding itself)
            reachable_count = 0
            for i in range(n):
                if i != city and distances[i] <= distanceThreshold:
                    reachable_count += 1
            
            # Update result
            if reachable_count < min_reachable:
                min_reachable = reachable_count
                result_city = city
            elif reachable_count == min_reachable and city > result_city:
                result_city = city
        
        return result_city
    
    # Method 3: Dijkstra with Early Termination
    def findTheCityDijkstraOptimized(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        min_reachable = n
        result_city = 0
        
        for city in range(n):
            # Priority queue for Dijkstra
            heap = [(0, city)]
            distances = [float('inf')] * n
            distances[city] = 0
            visited = [False] * n
            
            while heap:
                curr_dist, node = heapq.heappop(heap)
                
                if visited[node]:
                    continue
                
                visited[node] = True
                
                # Early termination: skip neighbors if current distance already exceeds threshold
                if curr_dist > distanceThreshold:
                    continue
                
                # Explore neighbors
                for neighbor, weight in graph[node]:
                    if not visited[neighbor]:
                        new_dist = curr_dist + weight
                        if new_dist < distances[neighbor]:
                            distances[neighbor] = new_dist
                            if new_dist <= distanceThreshold:
                                heapq.heappush(heap, (new_dist, neighbor))
            
            # Count reachable cities
            reachable_count = 0
            for i in range(n):
                if i != city and distances[i] <= distanceThreshold:
                    reachable_count += 1
            
            # Update result
            if reachable_count < min_reachable:
                min_reachable = reachable_count
                result_city = city
            elif reachable_count == min_reachable and city > result_city:
                result_city = city
        
        return result_city
    
    # Method 4: Bellman-Ford from each node (Alternative to Floyd Warshall)
    def findTheCityBellmanFord(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # We'll run Bellman-Ford from each node
        min_reachable = n
        result_city = 0
        
        for city in range(n):
            # Initialize distances
            distances = [float('inf')] * n
            distances[city] = 0
            
            # Relax edges n-1 times
            for _ in range(n - 1):
                updated = False
                for u, v, w in edges:
                    if distances[u] != float('inf') and distances[u] + w < distances[v]:
                        distances[v] = distances[u] + w
                        updated = True
                    if distances[v] != float('inf') and distances[v] + w < distances[u]:
                        distances[u] = distances[v] + w
                        updated = True
                
                if not updated:
                    break
            
            # Count reachable cities
            reachable_count = 0
            for i in range(n):
                if i != city and distances[i] <= distanceThreshold:
                    reachable_count += 1
            
            # Update result
            if reachable_count < min_reachable:
                min_reachable = reachable_count
                result_city = city
            elif reachable_count == min_reachable and city > result_city:
                result_city = city
        
        return result_city


def run_all_city_examples():
    print("=" * 60)
    print("FIND THE CITY WITH SMALLEST NEIGHBORS AT THRESHOLD DISTANCE")
    print("=" * 60)
    
    solution = SmallestNeighborsAtThreshold()
    
    # Example 1
    print("\nExample 1:")
    n1 = 4
    edges1 = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distanceThreshold1 = 4
    
    result_fw1 = solution.findTheCityFloydWarshall(n1, edges1, distanceThreshold1)
    result_dijkstra1 = solution.findTheCityDijkstra(n1, edges1, distanceThreshold1)
    result_opt1 = solution.findTheCityDijkstraOptimized(n1, edges1, distanceThreshold1)
    result_bf1 = solution.findTheCityBellmanFord(n1, edges1, distanceThreshold1)
    
    print(f"Floyd-Warshall: City {result_fw1}")
    print(f"Dijkstra: City {result_dijkstra1}")
    print(f"Optimized Dijkstra: City {result_opt1}")
    print(f"Bellman-Ford: City {result_bf1}")
    print("Expected: City 3")
    
    # Example 2
    print("\nExample 2:")
    n2 = 5
    edges2 = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    distanceThreshold2 = 2
    
    result_fw2 = solution.findTheCityFloydWarshall(n2, edges2, distanceThreshold2)
    result_dijkstra2 = solution.findTheCityDijkstra(n2, edges2, distanceThreshold2)
    
    print(f"Floyd-Warshall: City {result_fw2}")
    print(f"Dijkstra: City {result_dijkstra2}")
    print("Expected: City 0")
    
    # Example 3 (From LeetCode)
    print("\nExample 3:")
    n3 = 6
    edges3 = [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]]
    distanceThreshold3 = 20
    
    result_fw3 = solution.findTheCityFloydWarshall(n3, edges3, distanceThreshold3)
    print(f"Floyd-Warshall: City {result_fw3}")
    print("Expected: City 5")
    
    # Edge Case: All cities reachable
    print("\nEdge Case - All cities reachable:")
    n4 = 3
    edges4 = [[0, 1, 1], [1, 2, 1], [0, 2, 2]]
    distanceThreshold4 = 3
    
    result_fw4 = solution.findTheCityFloydWarshall(n4, edges4, distanceThreshold4)
    print(f"Floyd-Warshall: City {result_fw4}")
    print("Expected: City 2 (largest city with max reachable count)")
    
    print("\n" + "=" * 60)

# Performance Comparison
class PerformanceComparison:
    @staticmethod
    def analyze_methods():
        print("\nPERFORMANCE ANALYSIS")
        print("-" * 40)
        
        complexities = {
            "Floyd-Warshall": {
                "Time Complexity": "O(n³)",
                "Space Complexity": "O(n²)",
                "Best For": "Dense graphs, when all-pairs shortest path needed"
            },
            "Dijkstra from each node": {
                "Time Complexity": "O(n * (E log n))",
                "Space Complexity": "O(n + E)",
                "Best For": "Sparse graphs (E << n²)"
            },
            "Optimized Dijkstra": {
                "Time Complexity": "O(n * (E log n)) with early termination",
                "Space Complexity": "O(n + E)",
                "Best For": "Sparse graphs with small thresholds"
            },
            "Bellman-Ford from each node": {
                "Time Complexity": "O(n² * E)",
                "Space Complexity": "O(n)",
                "Best For": "Graphs with negative weights (not needed here)"
            }
        }
        
        for method, info in complexities.items():
            print(f"\n{method}:")
            for key, value in info.items():
                print(f"  {key}: {value}")
        
        print("\nRecommendation:")
        print("1. For n ≤ 100: Floyd-Warshall is simplest")
        print("2. For sparse graphs: Dijkstra from each node")
        print("3. For very sparse graphs with small thresholds: Optimized Dijkstra")

if __name__ == "__main__":
    run_all_city_examples()
    PerformanceComparison.analyze_methods()