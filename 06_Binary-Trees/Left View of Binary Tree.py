from collections import deque
from typing import Optional, List

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LeftView(root: Optional[Node]) -> List[int]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        # The first node in the queue at each level is the leftmost node
        result.append(queue[0].data)
        
        # Process all nodes at current level
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            
            # Add children for next level (left first, then right)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Example
print("Left View of Binary Tree:")
print("\nTree structure:")
print("""
        1
       / \\
      2   3
     / \\   \\
    4   5   6
       /
      7
""")

# Build the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.right.left = Node(7)

result = LeftView(root)

print(f"\nLeft view: {result}")

print("\nExplanation:")
print("Level 0 (depth 0): Leftmost node is 1")
print("Level 1 (depth 1): Leftmost node is 2")
print("Level 2 (depth 2): Leftmost node is 4")
print("Level 3 (depth 3): Leftmost node is 7")
print("\nResult: [1, 2, 4, 7]")

print("\nAlternative visualization:")
print("Stand to the left of the tree and look:")
print("""
    You see:    1
               /
              2
             /
            4
             \\
              7
""")