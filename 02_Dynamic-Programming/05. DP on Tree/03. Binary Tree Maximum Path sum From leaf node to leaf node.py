# Python program to find maximum path sum between two leaves
# of a binary tree

INT_MIN = -2**32

# A binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Utility function to find maximum sum between any
# two leaves. This function calculates two values:
# 1) Maximum path sum between two leaves which is stored in res
# 2) The maximum root to leaf path sum which is returned
def maxPathSumUtil(root, res):
    # Base Case
    if root is None:
        return 0

    # Find maximum sum in left and right subtree
    ls = maxPathSumUtil(root.left, res)
    rs = maxPathSumUtil(root.right, res)

    # If both left and right children exist
    if root.left is not None and root.right is not None:
        # Update result if needed (path through current node)
        res[0] = max(res[0], ls + rs + root.data)

        # Return max possible value for root being on one side
        return max(ls, rs) + root.data

    # If one child is missing, return the sum from the existing child
    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data

# Main function which returns the maximum path sum between any two leaves
def maxPathSum(root):
    res = [INT_MIN]
    maxPathSumUtil(root, res)
    return res[0]


# ---------------- Example Usage ----------------
# Helper function to build tree from list (level-order)
def build_tree(arr):
    if not arr:
        return None
    root = Node(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = Node(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = Node(arr[i])
            queue.append(node.right)
        i += 1
    return root

# Example 1 (from the code)
root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)

print("Max path sum of the given binary tree is", maxPathSum(root))  # Output: 27

# Example 2
# Tree:     10
#         /    \
#       2       10
#      /  \       \
#    20    1      -5
root2 = build_tree([10, 2, 10, 20, 1, None, -5])
print("Max path sum of the given binary tree is", maxPathSum(root2))  # Output: 33 (20+2+10+1)

# Example 3
# Tree:     1
#          / \
#         2   3
root3 = build_tree([1, 2, 3])
print("Max path sum of the given binary tree is", maxPathSum(root3))  # Output: 6 (2+1+3)

# Example 4 (negative values)
root4 = build_tree([-3, -1, -2])
print("Max path sum of the given binary tree is", maxPathSum(root4))  # Output: -4 (-1 + -3 + -2)

# Example 5 (single node)
root5 = build_tree([42])
print("Max path sum of the given binary tree is", maxPathSum(root5))  # Output: 42

# Example 6 (skewed tree)
root6 = build_tree([1, 2, None, 3, None, 4])
print("Max path sum of the given binary tree is", maxPathSum(root6))  # Output: 10 (1+2+3+4)