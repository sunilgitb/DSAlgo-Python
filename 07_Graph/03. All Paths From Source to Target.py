from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Find all paths from node 0 to node n-1 in a DAG
        
        Args:
            graph: Adjacency list where graph[i] = list of nodes reachable from i
        
        Returns:
            List of all paths from 0 to n-1
        """
        n = len(graph)
        result = []
        
        print(f"Graph has {n} nodes")
        print("Adjacency list:")
        for i, neighbors in enumerate(graph):
            print(f"  Node {i} -> {neighbors}")
        print("\n" + "=" * 50)
        
        def dfs(path, current_node, depth=0):
            """
            Depth-first search to find all paths
            
            Args:
                path: Current path from source
                current_node: Current node being explored
                depth: Depth for visualization indentation
            """
            indent = "  " * depth
            print(f"{indent}DFS at node {current_node}, current path: {path}")
            
            # Add current node to path
            current_path = path + [current_node]
            
            # If we reached the target
            if current_node == n - 1:
                print(f"{indent}✓ Found path: {current_path}")
                result.append(current_path)
                return
            
            # Explore all neighbors
            print(f"{indent}  Neighbors of {current_node}: {graph[current_node]}")
            for neighbor in graph[current_node]:
                dfs(current_path, neighbor, depth + 1)
        
        dfs([], 0)
        return result
    
    def allPathsSourceTargetBacktrack(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Alternative implementation using backtracking (modifying path in place)
        """
        n = len(graph)
        result = []
        path = []
        
        def backtrack(node):
            path.append(node)
            
            if node == n - 1:
                result.append(path[:])  # Make a copy
            else:
                for neighbor in graph[node]:
                    backtrack(neighbor)
            
            path.pop()  # Backtrack
        
        backtrack(0)
        return result


def run_examples():
    print("=" * 60)
    print("LEETCODE 797: ALL PATHS FROM SOURCE TO TARGET")
    print("=" * 60)
    
    solution = Solution()
    
    # Example 1: Simple graph
    print("\nExample 1:")
    graph1 = [[1, 2], [3], [3], []]
    print(f"Graph: {graph1}")
    
    print("\nDFS Traversal:")
    result1 = solution.allPathsSourceTarget(graph1)
    print(f"\nAll paths: {result1}")
    
    # Example 2: More complex graph
    print("\n" + "=" * 60)
    print("\nExample 2:")
    graph2 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(f"Graph: {graph2}")
    
    print("\nDFS Traversal:")
    result2 = solution.allPathsSourceTarget(graph2)
    print(f"\nAll paths: {result2}")
    
    # Example 3: Linear graph
    print("\n" + "=" * 60)
    print("\nExample 3:")
    graph3 = [[1], [2], [3], [4], []]
    print(f"Graph: {graph3}")
    
    result3 = solution.allPathsSourceTarget(graph3)
    print(f"\nAll paths: {result3}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_examples()