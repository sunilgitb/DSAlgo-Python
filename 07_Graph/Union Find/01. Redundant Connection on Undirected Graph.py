from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        LeetCode 684: Redundant Connection
        Using Union-Find to detect cycle in undirected graph
        
        Args:
            edges: List of edges [u, v] where u,v are nodes (1 to n)
        
        Returns:
            The edge that can be removed to make the graph a tree
        """
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}
        
        print("Initial parent array:")
        print("  " + str([(node, parent) for node, parent in parent.items()]))
        print()
        
        def find(node):
            """Find root of node with path compression"""
            while parent[node] != node:
                node = parent[node]
            return node
        
        def union(node1, node2):
            """Union two nodes"""
            root1 = find(node1)
            root2 = find(node2)
            
            print(f"  Union({node1}, {node2}):")
            print(f"    find({node1}) = {root1}, find({node2}) = {root2}")
            
            if root1 != root2:
                parent[root2] = root1
                print(f"    Made parent[{root2}] = {root1}")
            else:
                print(f"    Same root! This edge would create a cycle")
            
            print(f"    Parent array: {[(node, p) for node, p in parent.items()]}")
            
            return root1 != root2  # Returns True if union was successful (no cycle)
        
        print("Processing edges:")
        print("-" * 50)
        
        for i, edge in enumerate(edges):
            u, v = edge
            print(f"Edge {i+1}: [{u}, {v}]")
            
            if not union(u, v):  # If union returns False, nodes already connected
                print(f"→ Cycle detected! Return edge: {edge}")
                print("-" * 50)
                return edge
        
        return []  # Should never reach here for valid input


# Test the solution with examples
def run_examples():
    print("=" * 60)
    print("LEETCODE 684: REDUNDANT CONNECTION")
    print("=" * 60)
    
    solution = Solution()
    
    # Example 1: Basic cycle
    print("\nExample 1:")
    edges1 = [[1, 2], [1, 3], [2, 3]]
    print(f"Edges: {edges1}")
    print(f"Graph: 1-2-3 (with edge 2-3 creating triangle)")
    result1 = solution.findRedundantConnection(edges1)
    print(f"Redundant edge: {result1}")
    
    # Example 2: Longer cycle
    print("\n\nExample 2:")
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(f"Edges: {edges2}")
    print(f"Graph: 1-2-3-4 (with edge 1-4 creating square)")
    result2 = solution.findRedundantConnection(edges2)
    print(f"Redundant edge: {result2}")
    
    # Example 3: Complex case
    print("\n\nExample 3:")
    edges3 = [[1, 2], [2, 3], [2, 4], [4, 5], [1, 5]]
    print(f"Edges: {edges3}")
    print(f"Graph: Chain with redundant connection at end")
    result3 = solution.findRedundantConnection(edges3)
    print(f"Redundant edge: {result3}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_examples()