# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        mem = {}
        def dfs(root, can_steal):

            if root == None:
                return 0

            if (root, can_steal) in mem:
                return mem[(root, can_steal)]

            if can_steal:
                res =  max(root.val + dfs(root.left, not can_steal) + dfs(root.right, not can_steal),
                            dfs(root.left, can_steal) + dfs(root.right, can_steal)
                        )
            else:
                res = dfs(root.left, not can_steal) + dfs(root.right, not can_steal)

            mem[(root, can_steal)] = res
            return res
        
        return dfs(root, True)
