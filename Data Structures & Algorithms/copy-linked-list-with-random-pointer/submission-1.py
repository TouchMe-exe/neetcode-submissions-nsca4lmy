"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        random_map = {}

        def clone(head):
            if head == None:
                return None
            node = Node(head.val)
            random_map[head] = node
            node.next = clone(head.next)
            node.random = random_map[head.random] if head.random else None
            return node

        return clone(head)