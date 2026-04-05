# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def find(root, curr_max):
            if not root:
                return 0

            if curr_max <= root.val:
                curr_max = root.val
                return 1 + find(root.left, curr_max) + find(root.right, curr_max)
            
            else:
                return find(root.left, curr_max) + find(root.right, curr_max)
        
        return find(root, root.val)

