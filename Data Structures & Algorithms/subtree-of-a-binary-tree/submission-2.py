# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same(p,q):
            if not p and not q:
                return True
            
            if p and q and p.val == q.val:
                return is_same(p.left, q.left) and is_same(p.right, q.right)

            else:
                return False
        
        def traverse(root):
            if root == None:
                return False

            #if root.val == subRoot.val:    
            if is_same(root,subRoot):
                    return True

            else:
                return traverse(root.left) or traverse(root.right)
        
        return traverse(root)
               