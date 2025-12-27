from typing import List
from collections import deque, defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        Minimum number of cable reconnections to connect all computers
        
        Args:
            n: Number of computers (0 to n-1)
            connections: List of cable connections [a, b]
        
        Returns:
            Minimum operations or -1 if impossible
        """
        # Edge case: no computers
        if n == 0:
            return 0
        
        print(f"Total computers: {n}")
        print(f"Total connections: {len(connections)}")
        print(f"Connections: {connections}")
        print("-" * 50)
        
        # Build adjacency list
        adjList = {i: [] for i in range(n)}
        for a, b in connections:
            adjList[a].append(b)
            adjList[b].append(a)
        
        print("Network graph:")
        for computer in adjList:
            print(f"  Computer {computer}: connected to {adjList[computer]}")
        
        # Track visited computers
        visited = [False] * n
        
        # Count connected components using BFS
        components = 0
        queue = deque()
        
        print("\nFinding connected components:")
        print("-" * 30)
        
        for computer in range(n):
            if not visited[computer]:
                components += 1
                print(f"\nStarting BFS for component {components} from computer {computer}")
                
                queue.append(computer)
                visited[computer] = True
                
                component_nodes = [computer]
                
                while queue:
                    current = queue.popleft()
                    
                    # Explore neighbors
                    for neighbor in adjList[current]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            component_nodes.append(neighbor)
                            print(f"  Found connection: {current} ↔ {neighbor}")
                
                print(f"  Component {components} has computers: {sorted(component_nodes)}")
        
        print("\n" + "=" * 50)
        print(f"Total connected components: {components}")
        print(f"Total cables available: {len(connections)}")
        print(f"Minimum cables needed to connect all: {n-1}")
        
        # Check if possible
        if len(connections) < n - 1:
            print(f"\n❌ IMPOSSIBLE: Need at least {n-1} cables, but only have {len(connections)}")
            return -1
        
        # Calculate operations needed
        operations = components - 1
        print(f"\n✅ POSSIBLE: Need {operations} cable reconnections")
        print(f"   (Connect {components} components using {components-1} cables)")
        
        return operations
    
    def makeConnectedDFS(self, n: int, connections: List[List[int]]) -> int:
        """
        Alternative DFS implementation
        """
        # Build graph
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        # Check if enough cables
        if len(connections) < n - 1:
            return -1
        
        # Count components using DFS
        visited = [False] * n
        components = 0
        
        def dfs(node):
            stack = [node]
            visited[node] = True
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
        
        for i in range(n):
            if not visited[i]:
                components += 1
                dfs(i)
        
        return components - 1
    
    def makeConnectedUnionFind(self, n: int, connections: List[List[int]]) -> int:
        """
        Union-Find implementation (most efficient)
        """
        if len(connections) < n - 1:
            return -1
        
        parent = list(range(n))
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return 0  # Already connected
            
            # Union by rank
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            
            return 1  # Successfully connected
        
        components = n  # Start with n components (each computer separate)
        for a, b in connections:
            if union(a, b):
                components -= 1  # Merged two components
        
        return components - 1


# Driver Code
def main():
    print("=" * 70)
    print("LEETCODE 1319: NUMBER OF OPERATIONS TO MAKE NETWORK CONNECTED")
    print("=" * 70)
    
    solution = Solution()
    
    # Example 1: Can connect with 1 operation
    print("\nExample 1:")
    n1 = 4
    connections1 = [[0, 1], [0, 2], [1, 2]]
    print(f"Computers: {n1}")
    print(f"Connections: {connections1}")
    
    result1 = solution.makeConnected(n1, connections1)
    print(f"\nResult: {result1} operations needed")
    
    # Example 2: Need 2 operations
    print("\n" + "=" * 70)
    print("\nExample 2:")
    n2 = 6
    connections2 = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    print(f"Computers: {n2}")
    print(f"Connections: {connections2}")
    
    result2 = solution.makeConnected(n2, connections2)
    print(f"\nResult: {result2} operations needed")
    
    # Example 3: Impossible (not enough cables)
    print("\n" + "=" * 70)
    print("\nExample 3:")
    n3 = 6
    connections3 = [[0, 1], [0, 2], [0, 3], [1, 2]]
    print(f"Computers: {n3}")
    print(f"Connections: {connections3}")
    
    result3 = solution.makeConnected(n3, connections3)
    print(f"\nResult: {result3}")
    
    # Example 4: Already connected
    print("\n" + "=" * 70)
    print("\nExample 4:")
    n4 = 5
    connections4 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(f"Computers: {n4}")
    print(f"Connections: {connections4}")
    
    result4 = solution.makeConnected(n4, connections4)
    print(f"\nResult: {result4} operations needed")
    
    # Example 5: Disconnected with extra cables
    print("\n" + "=" * 70)
    print("\nExample 5:")
    n5 = 8
    connections5 = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3],
                    [4, 5], [4, 6], [5, 6],
                    [7, 0]]  # Extra cable connecting component 3 to component 1
    print(f"Computers: {n5}")
    print(f"Connections: {connections5}")
    
    result5 = solution.makeConnected(n5, connections5)
    print(f"\nResult: {result5} operations needed")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()