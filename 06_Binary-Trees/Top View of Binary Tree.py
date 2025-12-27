from collections import deque
from typing import Optional, List

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def topView(self, root: Optional[Node]) -> List[int]:
        if not root:
            return []
        
        # Dictionary to store the first node at each horizontal distance
        distance_dict = {}
        
        # Queue for BFS: (node, horizontal_distance)
        # Using deque for efficient popleft operations
        queue = deque([(root, 0)])
        
        while queue:
            node, distance = queue.popleft()
            
            # Only store the first node at each distance (top view)
            if distance not in distance_dict:
                distance_dict[distance] = node.data
            
            # Add children with updated distances
            if node.left:
                queue.append((node.left, distance - 1))
            if node.right:
                queue.append((node.right, distance + 1))
        
        # Sort distances from leftmost to rightmost
        sorted_distances = sorted(distance_dict.keys())
        
        # Build result in order from left to right
        result = [distance_dict[dist] for dist in sorted_distances]
        
        return result

# Example
print("Top View of Binary Tree:")
print("\nTree structure:")
print("""
        1
       /  \\
      2    3
     / \\  / \\
    4   5 6  7
""")

# Build the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()
result = solution.topView(root)

print(f"\nTop view: {result}")

print("\nExplanation (horizontal distances):")
print("Node 1: distance 0 (root)")
print("Node 2: distance -1, Node 3: distance +1")
print("Node 4: distance -2, Node 5: distance 0, Node 6: distance 0, Node 7: distance +2")

print("\nFor each distance, top view takes the first node encountered:")
print("Distance -2: First node is 4")
print("Distance -1: First node is 2")
print("Distance 0: First node is 1 (encountered before 5 and 6)")
print("Distance +1: First node is 3")
print("Distance +2: First node is 7")

print("\nResult from left to right: [4, 2, 1, 3, 7]")

print("\n" + "="*60)
print("\nMore complex example:")
print("\nTree structure:")
print("""
        10
       /  \\
      5    15
     / \\   / \\
    2   8 12  20
         \\
          9
""")

# Build a more complex tree
root2 = Node(10)
root2.left = Node(5)
root2.right = Node(15)
root2.left.left = Node(2)
root2.left.right = Node(8)
root2.right.left = Node(12)
root2.right.right = Node(20)
root2.left.right.right = Node(9)

result2 = solution.topView(root2)
print(f"\nTop view: {result2}")

print("\nHorizontal distances and first nodes:")
print("Distance -2: Node 2")
print("Distance -1: Node 5")
print("Distance 0: Node 10")
print("Distance +1: Node 15")
print("Distance +2: Node 20")
print("Note: Node 8 (distance 0) and Node 9 (distance +1) are not visible from top")
print("      because Node 10 and Node 15 block them respectively")