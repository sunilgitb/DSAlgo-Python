from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        LeetCode 685: Redundant Connection II
        Handles two cases in directed graphs:
        1. A node has two parents (invalid indegree = 2)
        2. There is a cycle in the graph
        
        Returns the edge that can be removed to make it a valid rooted tree
        """
        n = len(edges)
        
        # Step 1: Find if any node has two parents
        parent = [0] * (n + 1)  # Track parent of each node
        candidate1, candidate2, conflict_child = None, None, None
        
        print("Step 1: Checking for nodes with two parents")
        print("-" * 50)
        
        for i, (u, v) in enumerate(edges):
            print(f"  Edge {i+1}: [{u} -> {v}]")
            
            if parent[v] != 0:  # Node v already has a parent
                # Found a node with two parents!
                candidate1 = [parent[v], v]  # First parent edge
                candidate2 = [u, v]          # Second parent edge
                conflict_child = v
                edges[i][0] = 0  # Temporarily remove current edge
                print(f"  ⚠️  Node {v} has two parents!")
                print(f"     First parent: {parent[v]} (edge: {candidate1})")
                print(f"     Second parent: {u} (edge: {candidate2})")
                print(f"     Temporarily removing edge {candidate2}")
            else:
                parent[v] = u
            print(f"  Parent array: {parent[1:]}")
        
        # Step 2: Use Union-Find to check for cycles
        print("\nStep 2: Checking for cycles with Union-Find")
        print("-" * 50)
        
        # Initialize Union-Find
        uf_parent = list(range(n + 1))
        
        def find(x: int) -> int:
            """Find with path compression"""
            if uf_parent[x] != x:
                uf_parent[x] = find(uf_parent[x])
            return uf_parent[x]
        
        for i, (u, v) in enumerate(edges):
            if u == 0:  # Skip the temporarily removed edge
                print(f"  Edge {i+1}: [{u} -> {v}] (skipped - temporarily removed)")
                continue
                
            print(f"  Edge {i+1}: [{u} -> {v}]")
            
            root_u = find(u)
            root_v = find(v)
            
            print(f"    find({u}) = {root_u}, find({v}) = {root_v}")
            
            if root_u == root_v:
                # Cycle detected!
                print(f"    ⚠️  Cycle detected! {u} and {v} are already connected")
                if candidate1:
                    # Case 2.1: Node has two parents AND removing candidate2 creates cycle
                    # So candidate1 must be the bad edge
                    print(f"    Removing candidate2 created cycle, so candidate1 is the bad edge")
                    return candidate1
                else:
                    # Case 2: Simple cycle (no double parent)
                    print(f"    Simple cycle found. Return current edge: [{u}, {v}]")
                    return [u, v]
            else:
                # Union the two nodes
                uf_parent[root_v] = root_u
                print(f"    Union: parent[{root_v}] = {root_u}")
                print(f"    UF Parent array: {uf_parent[1:]}")
        
        # Step 3: If we get here, no cycle was found
        # So the problem was just a double parent, and removing candidate2 fixed it
        print("\nStep 3: No cycles found")
        print("-" * 50)
        print(f"  The graph had a node with two parents but no cycle")
        print(f"  Removing candidate2 ({candidate2}) fixed the issue")
        return candidate2


def run_examples():
    print("=" * 70)
    print("LEETCODE 685: REDUNDANT CONNECTION II (DIRECTED GRAPH)")
    print("=" * 70)
    
    solution = Solution()
    
    # Example 1: Node with two parents (no cycle)
    print("\nExample 1: Node with two parents, no cycle")
    edges1 = [[1, 2], [1, 3], [2, 3]]
    print(f"Edges: {edges1}")
    result1 = solution.findRedundantDirectedConnection(edges1)
    print(f"\nResult: Redundant edge = {result1}")
    
    # Example 2: Cycle in graph (no double parent)
    print("\n" + "=" * 70)
    print("\nExample 2: Cycle in graph, no double parent")
    edges2 = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    print(f"Edges: {edges2}")
    result2 = solution.findRedundantDirectedConnection(edges2)
    print(f"\nResult: Redundant edge = {result2}")
    
    # Example 3: Node with two parents AND cycle
    print("\n" + "=" * 70)
    print("\nExample 3: Node with two parents AND cycle")
    edges3 = [[2, 1], [3, 1], [4, 2], [1, 4]]
    print(f"Edges: {edges3}")
    result3 = solution.findRedundantDirectedConnection(edges3)
    print(f"\nResult: Redundant edge = {result3}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    run_examples()