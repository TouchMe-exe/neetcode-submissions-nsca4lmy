# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = -float('inf')

        def dfs(root):

            nonlocal max_sum

            if root == None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            res = root.val + max(left + right, left, right, 0) 
            node_max_sum = root.val + max(left, right, 0)

            max_sum = max(max_sum, res)

            return node_max_sum
        
        dfs(root)

        return max_sum





