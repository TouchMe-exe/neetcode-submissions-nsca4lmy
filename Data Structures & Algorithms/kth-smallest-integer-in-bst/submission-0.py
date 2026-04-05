# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cnt = k
        res = 0
        def inorder(root):

            nonlocal cnt, res

            if root == None:
                return res
                
            inorder(root.left)
            cnt -= 1
            if cnt == 0:
                res = root.val
            inorder(root.right)

            return res
        
        return inorder(root)



            