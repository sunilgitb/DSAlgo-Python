# https://practice.geeksforgeeks.org/problems/mirror-tree/1#

# User function Template for python3
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def mirror(self,root):
        
        def solve(root):
            if not root: 
                return
            solve(root.left)
            solve(root.right)
            l = root.left
            r = root.right
            root.left = r
            root.right = l
            
        solve(root)
        return root

# Time: O(N)
# Space: O(1)
# N is the number of nodes in the binary tree

# Example Usage:
# Constructing a binary tree
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
solution = Solution()
mirrored_root = solution.mirror(root)
# Print or traverse the mirrored tree to verify:
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.data, end=' ')
        print_inorder(node.right)
print_inorder(mirrored_root)


# The mirrored tree will be:
#         1
#        / \
#       3   2
#      /   / \
#     6   5   4

