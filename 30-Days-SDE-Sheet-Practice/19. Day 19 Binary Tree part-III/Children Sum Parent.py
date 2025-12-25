# https://practice.geeksforgeeks.org/problems/children-sum-parent/1/#
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        if not root or (not root.left and not root.right): 
            return 1
        else:
            left_data = root.left.data if root.left else 0
            right_data = root.right.data if root.right else 0
            
            if (root.data == left_data + right_data) and self.isSumProperty(root.left) and self.isSumProperty(root.right):
                return 1
            else:
                return 0

# Time : O(N)
# SPace: O(1)

# Example usage
# Definition for a binary tree node compatible with this solution
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    sol = Solution()

    # Simple valid tree:
    #      10
    #     /  \
    #    8    2
    root1 = Node(10, Node(8), Node(2))
    print("Tree1 satisfies children sum property:", bool(sol.isSumProperty(root1)))  # True

    # Simple invalid tree:
    #      10
    #     /  \
    #    5    3
    root2 = Node(10, Node(5), Node(3))
    print("Tree2 satisfies children sum property:", bool(sol.isSumProperty(root2)))  # False

    # Larger valid tree:
    #          26
    #         /  \
    #       10    16
    #      / \   / \
    #     4  6  7   9
    root3 = Node(26, Node(10, Node(4), Node(6)), Node(16, Node(7), Node(9)))
    print("Tree3 satisfies children sum property:", bool(sol.isSumProperty(root3)))  # True
