from typing import List
from collections import defaultdict

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        """
        Determine if we can add at most 2 edges to make all node degrees even
        
        Args:
            n: Number of nodes (1 to n)
            edges: List of existing edges
        
        Returns:
            True if possible, False otherwise
        """
        # Build adjacency list
        adjList = {i: set() for i in range(1, n + 1)}
        for a, b in edges:
            adjList[a].add(b)
            adjList[b].add(a)
        
        # Find nodes with odd degree
        odd_nodes = [i for i in adjList if len(adjList[i]) % 2 == 1]
        
        print(f"Total nodes: {n}")
        print(f"Total edges: {len(edges)}")
        print(f"Nodes with odd degree: {odd_nodes}")
        print(f"Number of odd degree nodes: {len(odd_nodes)}")
        print("-" * 50)
        
        # Helper function to check if we can add an edge between two nodes
        def can_add_edge(a, b):
            """Return True if edge (a,b) doesn't already exist"""
            return b not in adjList[a]
        
        def analyze_case_2():
            """Analyze case with exactly 2 odd nodes"""
            a, b = odd_nodes[0], odd_nodes[1]
            print(f"Case: 2 odd nodes ({a}, {b})")
            
            # Option 1: Directly connect the two odd nodes
            print(f"  Option 1: Connect {a} - {b}")
            if can_add_edge(a, b):
                print(f"    ✓ Possible (edge doesn't exist)")
                return True
            else:
                print(f"    ✗ Not possible (edge already exists)")
            
            # Option 2: Connect both to a common node
            print(f"  Option 2: Find common node to connect both")
            for node in range(1, n + 1):
                if node != a and node != b and can_add_edge(a, node) and can_add_edge(b, node):
                    print(f"    ✓ Possible via node {node}")
                    return True
            print(f"    ✗ No common node found")
            return False
        
        def analyze_case_4():
            """Analyze case with exactly 4 odd nodes"""
            a, b, c, d = odd_nodes
            print(f"Case: 4 odd nodes ({a}, {b}, {c}, {d})")
            
            # Check all possible pairings
            pairings = [
                [(a, b), (c, d)],
                [(a, c), (b, d)],
                [(a, d), (b, c)]
            ]
            
            for i, (pair1, pair2) in enumerate(pairings, 1):
                node1, node2 = pair1
                node3, node4 = pair2
                print(f"  Option {i}: Connect {node1}-{node2} and {node3}-{node4}")
                
                if can_add_edge(node1, node2) and can_add_edge(node3, node4):
                    print(f"    ✓ Both edges can be added")
                    return True
                else:
                    if not can_add_edge(node1, node2):
                        print(f"    ✗ Edge {node1}-{node2} already exists")
                    if not can_add_edge(node3, node4):
                        print(f"    ✗ Edge {node3}-{node4} already exists")
            
            return False
        
        # Main logic
        if len(odd_nodes) == 0:
            print("Case: 0 odd nodes (all degrees already even)")
            print("✓ No edges need to be added")
            return True
        
        elif len(odd_nodes) == 2:
            result = analyze_case_2()
            print(f"\nResult: {result}")
            return result
        
        elif len(odd_nodes) == 4:
            result = analyze_case_4()
            print(f"\nResult: {result}")
            return result
        
        else:
            print(f"Case: {len(odd_nodes)} odd nodes")
            print(f"✗ Impossible: Need to add more than 2 edges")
            return False


def run_examples():
    print("=" * 60)
    print("LEETCODE 2508: ADD EDGES TO MAKE DEGREES OF ALL NODES EVEN")
    print("=" * 60)
    
    solution = Solution()
    
    # Example 1: 2 odd nodes that can be directly connected
    print("\nExample 1: 2 odd nodes, direct connection possible")
    n1 = 5
    edges1 = [[1,2], [2,3], [3,4], [4,2], [1,4], [2,5]]
    print(f"n = {n1}, edges = {edges1}")
    result1 = solution.isPossible(n1, edges1)
    print(f"Final result: {result1}")
    
    # Example 2: 2 odd nodes that need common node
    print("\n" + "=" * 60)
    print("\nExample 2: 2 odd nodes, need common node")
    n2 = 4
    edges2 = [[1,2], [1,3], [1,4]]
    print(f"n = {n2}, edges = {edges2}")
    result2 = solution.isPossible(n2, edges2)
    print(f"Final result: {result2}")
    
    # Example 3: 4 odd nodes
    print("\n" + "=" * 60)
    print("\nExample 3: 4 odd nodes")
    n3 = 4
    edges3 = [[1,2], [2,3], [3,4], [4,1]]
    print(f"n = {n3}, edges = {edges3}")
    result3 = solution.isPossible(n3, edges3)
    print(f"Final result: {result3}")
    
    # Example 4: Already all even
    print("\n" + "=" * 60)
    print("\nExample 4: All degrees already even")
    n4 = 4
    edges4 = [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
    print(f"n = {n4}, edges = {edges4}")
    result4 = solution.isPossible(n4, edges4)
    print(f"Final result: {result4}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_examples()