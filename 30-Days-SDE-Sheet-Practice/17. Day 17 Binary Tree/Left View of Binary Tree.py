# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1#

import collections

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def LeftView(root):
    final_ans = []
    q = collections.deque()
    q.append(root)
    if not root: return final_ans
				
    while q:
        final_ans.append(q[0].data)
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
    return final_ans
        
# Instead of using array as a queue we should use collections.deque()
# as pop() 0'th element from deque is of O(1) time.

# Time: O(N)
# Space: O(N)

# Example Usage:
# Constructing the following binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print(LeftView(root))  # Output: [1, 2, 4]

