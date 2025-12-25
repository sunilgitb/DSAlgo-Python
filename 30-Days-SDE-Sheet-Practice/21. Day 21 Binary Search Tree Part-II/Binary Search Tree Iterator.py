# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Optimal Approach
# Time: O(1) amortized per operation
# Space: O(H) where H = height of tree

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_all_left(root)

    def next(self) -> int:
        node = self.stack.pop()
        self._push_all_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _push_all_left(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left

# Construct BST
#        7
#       / \
#      3   15
#          / \
#         9  20

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

iterator = BSTIterator(root)

print(iterator.next())     # Output: 3
print(iterator.next())     # Output: 7
print(iterator.hasNext())  # Output: True
print(iterator.next())     # Output: 9
print(iterator.hasNext())  # Output: True
print(iterator.next())     # Output: 15
print(iterator.hasNext())  # Output: True
print(iterator.next())     # Output: 20
print(iterator.hasNext())  # Output: False
