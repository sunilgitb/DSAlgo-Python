class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    res = []
    
    tmp = []
    def inorder(root):
        if not root: return
        inorder(root.left)
        tmp.append(root.data)
        inorder(root.right)
    inorder(root)
    res.append(tmp)
    
    tmp = []
    def preorder(root):
        if not root: return
        tmp.append(root.data)
        preorder(root.left)
        preorder(root.right)
    preorder(root)
    res.append(tmp)
    
    tmp = []
    def postorder(root):
        if not root: return
        postorder(root.left)
        postorder(root.right)
        tmp.append(root.data)
    postorder(root)
    res.append(tmp)
    
    return res

# Example usage:
# Constructing a binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.right = BinaryTreeNode(6)
traversals = getTreeTraversal(root)
print("Inorder:", traversals[0])   # Output: [4, 2, 5, 1, 3, 6]
print("Preorder:", traversals[1])  # Output: [1, 2, 4, 5, 3, 6]
print("Postorder:", traversals[2]) # Output: [4, 5, 2, 6, 3, 1]