# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# https://youtu.be/u4JAi2JJhI8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    
    def serialize(self, root):
        res = []
        
        def preorder(root):
            if not root:
                res.append('N')
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        data = data.split(',')
        self.i = 0
        
        def preorder():
            if data[self.i] == 'N':
                self.i += 1
                return None
            
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = preorder()
            root.right = preorder()
            return root
        
        return preorder()
    

# Time Complexity: O(N)
# Space Complexity: O(N)
# Construct Binary Tree
#       1
#      / \
#     2   3
#        / \
#       4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()

# Serialize
serialized = codec.serialize(root)
print(serialized)
# Output: 1,2,N,N,3,4,N,N,5,N,N

# Deserialize
new_root = codec.deserialize(serialized)

# Verify by serializing again
print(codec.serialize(new_root))
# Output: 1,2,N,N,3,4,N,N,5,N,N
