from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []    # to store graph edges

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # If ranks are same, then make one as root and increment its rank
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's algorithm
    def KruskalMST(self):
        result = []  # This will store the resultant MST
        i = 0        # index variable for sorted edges
        e = 0        # index variable for result[]
        
        print("All edges in the graph (unsorted):")
        for u, v, w in self.graph:
            print(f"  {u} -- {v} (weight: {w})")
        print()

        # Step 1: Sort all edges by weight
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        print("Edges sorted by weight:")
        for u, v, w in self.graph:
            print(f"  {u} -- {v} (weight: {w})")
        print()

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        print("Kruskal's Algorithm Steps:")
        print("-" * 40)
        
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            # Step 2: Pick the smallest edge
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            print(f"Checking edge: {u} -- {v} (weight: {w})")
            print(f"  Root of {u}: {x}, Root of {v}: {y}")
            
            # If including this edge doesn't cause cycle
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                print(f"  ✓ ADDED to MST (no cycle)")
            else:
                print(f"  ✗ REJECTED (would create cycle)")
            print()

        # Calculate minimum cost and print results
        minimumCost = 0
        print("=" * 40)
        print("Edges in the constructed MST:")
        print("-" * 40)
        for u, v, weight in result:
            minimumCost += weight
            print(f"{u} -- {v} == {weight}")
        
        print("-" * 40)
        print(f"Total Minimum Cost: {minimumCost}")
        print("=" * 40)

# Driver code - Example 1
def run_example_1():
    print("=" * 40)
    print("KRUSKAL'S ALGORITHM - EXAMPLE 1")
    print("=" * 40)
    print("Graph with 4 vertices:")
    print("  Vertex 0, 1, 2, 3")
    print()
    
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
    
    # Function call
    g.KruskalMST()

# Run the example
if __name__ == "__main__":
    run_example_1()