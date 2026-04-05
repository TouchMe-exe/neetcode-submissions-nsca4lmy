# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def can_reach(root, target):
            
            if root == None:
                return False
            if root.val == target.val:
                return True
            else:
                return can_reach(root.left, target) or can_reach(root.right, target)

        def check_LCA(root , p, q):

            if root == None:
                return None

            left = check_LCA(root.left, p, q) 
            right = check_LCA(root.right, p, q)

            if left:
                return left
            if right:
                return right

            else:
                if can_reach(root, p) and can_reach(root, q):
                    return root
                else:
                    return None
        
        return check_LCA(root, p, q)
        