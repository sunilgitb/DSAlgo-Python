from typing import List
import collections

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Minimum road direction changes to make all paths lead to city 0
        
        Args:
            n: Number of cities (0 to n-1)
            connections: List of directed roads [from, to]
        
        Returns:
            Minimum number of direction changes
        """
        print(f"Total cities: {n}")
        print(f"Total roads: {len(connections)}")
        print(f"Roads: {connections}")
        print("-" * 50)
        
        # Build adjacency lists
        adj = {i: set() for i in range(n)}           # Undirected graph
        directedAdj = {i: set() for i in range(n)}   # Directed graph
        
        for a, b in connections:
            adj[a].add(b)
            adj[b].add(a)
            directedAdj[a].add(b)
            print(f"Road: City {a} → City {b}")
        
        print("\nGraph representation:")
        print("Undirected connections:")
        for city in adj:
            print(f"  City {city}: connected to {sorted(adj[city])}")
        
        print("\nDirected connections:")
        for city in directedAdj:
            if directedAdj[city]:
                print(f"  City {city}: points to {sorted(directedAdj[city])}")
        
        # BFS starting from city 0
        visited = [False] * n
        queue = collections.deque([0])
        changes = 0
        
        print("\n" + "=" * 50)
        print("BFS Traversal starting from City 0:")
        print("=" * 50)
        
        step = 1
        while queue:
            current = queue.popleft()
            visited[current] = True
            
            print(f"\nStep {step}: Visiting City {current}")
            print(f"  Current queue: {list(queue)}")
            
            # Check all neighbors
            for neighbor in adj[current]:
                if not visited[neighbor]:
                    print(f"  Checking neighbor City {neighbor}:")
                    
                    # If the road direction is FROM current TO neighbor
                    if neighbor in directedAdj[current]:
                        print(f"    Road direction: {current} → {neighbor}")
                        print(f"    ❌ WRONG DIRECTION! Need to reverse this road")
                        changes += 1
                    else:
                        print(f"    Road direction: {neighbor} → {current}")
                        print(f"    ✓ CORRECT DIRECTION (points to city 0)")
                    
                    # Add neighbor to queue for BFS
                    queue.append(neighbor)
                    print(f"    Added City {neighbor} to queue")
            
            step += 1
        
        print("\n" + "=" * 50)
        print(f"Total direction changes needed: {changes}")
        
        return changes
    
    def minReorderDFS(self, n: int, connections: List[List[int]]) -> int:
        """
        Alternative DFS recursive implementation
        """
        # Build graph
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, 1))   # 1 means needs reversal
            graph[b].append((a, 0))   # 0 means correct direction
        
        visited = [False] * n
        
        def dfs(city):
            visited[city] = True
            changes = 0
            for neighbor, needs_reversal in graph[city]:
                if not visited[neighbor]:
                    changes += needs_reversal
                    changes += dfs(neighbor)
            return changes
        
        return dfs(0)


# Driver Code
def main():
    print("=" * 70)
    print("LEETCODE 1466: REORDER ROUTES TO MAKE ALL PATHS LEAD TO CITY ZERO")
    print("=" * 70)
    
    solution = Solution()
    
    # Example 1: Simple star pattern
    print("\nExample 1:")
    n1 = 6
    connections1 = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    print(f"Cities: {n1}")
    print(f"Roads: {connections1}")
    
    result1 = solution.minReorder(n1, connections1)
    print(f"\nMinimum direction changes: {result1}")
    
    # Example 2: All roads point away from 0
    print("\n" + "=" * 70)
    print("\nExample 2:")
    n2 = 5
    connections2 = [[1, 0], [1, 2], [3, 2], [3, 4]]
    print(f"Cities: {n2}")
    print(f"Roads: {connections2}")
    
    result2 = solution.minReorder(n2, connections2)
    print(f"\nMinimum direction changes: {result2}")
    
    # Example 3: Already all roads point to 0
    print("\n" + "=" * 70)
    print("\nExample 3:")
    n3 = 3
    connections3 = [[1, 0], [2, 0]]
    print(f"Cities: {n3}")
    print(f"Roads: {connections3}")
    
    result3 = solution.minReorder(n3, connections3)
    print(f"\nMinimum direction changes: {result3}")
    
    # Example 4: Complex tree
    print("\n" + "=" * 70)
    print("\nExample 4:")
    n4 = 7
    connections4 = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    print(f"Cities: {n4}")
    print(f"Roads: {connections4}")
    
    result4 = solution.minReorder(n4, connections4)
    print(f"\nMinimum direction changes: {result4}")
    
    # Example 5: Mixed directions
    print("\n" + "=" * 70)
    print("\nExample 5:")
    n5 = 5
    connections5 = [[0, 1], [2, 1], [3, 2], [4, 3], [0, 4]]
    print(f"Cities: {n5}")
    print(f"Roads: {connections5}")
    
    result5 = solution.minReorder(n5, connections5)
    print(f"\nMinimum direction changes: {result5}")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()