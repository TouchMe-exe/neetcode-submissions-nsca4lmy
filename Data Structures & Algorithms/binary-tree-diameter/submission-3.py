# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def max_depth(root):
            if root == None:
                return 0
            return 1 + max(max_depth(root.left),max_depth(root.right))

        
        def traverse(root):
            if root == None:
                return 
            else:
                nonlocal result
                result = max(result, max_depth(root.left) + max_depth(root.right))
                traverse(root.left)
                traverse(root.right)

        traverse(root)
        return result