# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque()
        result = []
        q.append(root)

        def helper(node):
            q.append(node.left)
            q.append(node.right)

        
        def bfs():
            while q:
                len_q = len(q)
                layer = []
                for i in range(len_q):
                    node = q.popleft()
                    if node:
                        helper(node)
                        layer.append(node.val)
                if layer:
                    result.append(layer[-1])
        
        bfs()
        return result