from collections import deque
from typing import Optional, List

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def bottomView(self, root: Optional[Node]) -> List[int]:
        if not root:
            return []
        
        # Dictionary to store the last node at each horizontal distance
        dist_dict = {}
        
        # Queue for BFS: (node, horizontal_distance)
        queue = deque([(root, 0)])
        
        while queue:
            node, dist = queue.popleft()
            
            # For bottom view, we always update with the latest node at this distance
            # (since we're doing level order, later nodes are deeper/bottom)
            dist_dict[dist] = node.data
            
            # Add children with updated distances
            if node.left:
                queue.append((node.left, dist - 1))
            if node.right:
                queue.append((node.right, dist + 1))
        
        # Sort distances from leftmost to rightmost
        min_dist = min(dist_dict.keys())
        max_dist = max(dist_dict.keys())
        
        result = []
        for dist in range(min_dist, max_dist + 1):
            if dist in dist_dict:
                result.append(dist_dict[dist])
        
        return result

# Example
print("Bottom View of Binary Tree:")
print("\nTree structure:")
print("""
        20
       /  \\
      8    22
     / \\   / \\
    5   3 4   25
       / \\     
      10  14
""")

# Build the tree
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

solution = Solution()
result = solution.bottomView(root)

print(f"\nBottom view: {result}")

print("\nExplanation (horizontal distances):")
print("Node 20: distance 0")
print("Node 8: distance -1, Node 22: distance +1")
print("Node 5: distance -2, Node 3: distance 0, Node 4: distance 0, Node 25: distance +2")
print("Node 10: distance -1, Node 14: distance +1")
print("\nFor each distance, bottom view takes the deepest node:")
print("Distance -2: Node 5 (only node at this distance)")
print("Distance -1: Nodes 8 and 10 → deeper is 10")
print("Distance 0: Nodes 20, 3, 4 → deepest is 4")
print("Distance +1: Nodes 22 and 14 → deepest is 14")
print("Distance +2: Node 25 (only node at this distance)")
print("\nResult from left to right: [5, 10, 4, 14, 25]")