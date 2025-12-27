import heapq

def calculate_distances(graph, starting_vertex):
    """
    Dijkstra's algorithm for shortest path distances from starting_vertex.
    
    Args:
        graph: Dictionary of dictionaries {vertex: {neighbor: weight, ...}}
        starting_vertex: The source vertex
    
    Returns:
        Dictionary of shortest distances from starting_vertex to all vertices
    """
    # Initialize distances: infinity for all vertices except starting vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    
    # Priority queue: (distance, vertex)
    priority_queue = [(0, starting_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Skip if we found a better path already
        if current_distance > distances[current_vertex]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If found shorter path to neighbor, update and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example graph from your code
example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print("Dijkstra's Algorithm Example:")
print("\nGraph adjacency list with weights:")
for vertex, neighbors in example_graph.items():
    print(f"  {vertex}: {neighbors}")

print("\nVisual representation:")
print("""
        U ---2--- V
       / \\       / \\
      1   5     2   3
     /     \\   /     \\
    X---3---W---1---Y
     \\       /       /
      2     5       1
       \\   /       /
        V---3---Z
""")

# Run Dijkstra from vertex 'X'
source = 'X'
print(f"\nShortest distances from vertex '{source}':")
distances = calculate_distances(example_graph, source)

# Print distances in a nice format
for vertex in sorted(distances.keys()):
    if distances[vertex] == float('infinity'):
        print(f"  {vertex}: unreachable")
    else:
        print(f"  {vertex}: {distances[vertex]}")

print("\nStep-by-step shortest paths from X:")
print("X → U: direct = 1")
print("X → V: X → U → V = 1 + 2 = 3, or X → V direct = 2 → shortest = 2")
print("X → W: X → Y → W = 1 + 1 = 2")
print("X → Y: direct = 1")
print("X → Z: X → Y → Z = 1 + 1 = 2")

print("\n" + "="*60)
print("Complexity Analysis:")
print("V = 6 (vertices: U, V, W, X, Y, Z)")
print("E = 9 (total edges, counting both directions)")
print("\nTime Complexity Breakdown:")
print("1. Initialize distances: O(V) = O(6)")
print("2. Priority queue operations: O(E log E) = O(9 log 9) ≈ O(9 * 3.17) ≈ O(28.5)")
print("3. Edge relaxations: O(E) = O(9)")
print("Total: O(V + E log E) ≈ O(6 + 28.5) ≈ O(34.5)")

print("\nSpace Complexity:")
print("1. Distances dictionary: O(V) = O(6)")
print("2. Priority queue: O(E) in worst case = O(9)")
print("Total: O(V + E) = O(15)")

print("\n" + "="*60)
print("Key Dijkstra's Algorithm Concepts:")
print("1. Greedy algorithm: Always expands the closest vertex")
print("2. Requires non-negative edge weights")
print("3. Uses priority queue for efficient min-distance extraction")
print("4. Each vertex is processed once (when popped from queue)")
print("5. Can be modified to find actual paths, not just distances")

# Additional test from different source
print("\n" + "="*60)
print("\nShortest distances from vertex 'U':")
distances_u = calculate_distances(example_graph, 'U')
for vertex in sorted(distances_u.keys()):
    if distances_u[vertex] == float('infinity'):
        print(f"  {vertex}: unreachable")
    else:
        print(f"  {vertex}: {distances_u[vertex]}")

print("\nVerification of shortest path U → Z:")
print("Possible paths:")
print("1. U → X → Y → Z = 1 + 1 + 1 = 3")
print("2. U → W → Z = 5 + 5 = 10")
print("3. U → V → W → Z = 2 + 3 + 5 = 10")
print("4. U → V → X → Y → Z = 2 + 2 + 1 + 1 = 6")
print("Shortest: U → X → Y → Z = 3 ✓")