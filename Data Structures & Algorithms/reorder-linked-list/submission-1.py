# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def rec(root:ListNode,curr:ListNode)->ListNode:
            
            if not curr:
                return root
            
            root = rec(root,curr.next)

            if not root or not root.next:
                return None
            
            if root==curr or root.next==curr:
                curr.next=None
                return None


            temp=root.next
            root.next=curr
            curr.next=temp

            root=temp

            return root





        head=rec(head,head.next)