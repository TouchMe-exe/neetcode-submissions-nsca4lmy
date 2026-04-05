# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def rev(head, k):
            if k == right-left:
                return head
            else:
                temp = rev(head.next, k+1)
                head.next.next = head
                head.next = None

                return temp
        
        dummy = head
        curr = 0

        while curr<right:
            dummy = dummy.next
            curr += 1
        right_node = dummy

        curr = 0
        dummy = ListNode(0,head)

        while curr<left-1:
            dummy = dummy.next
            curr += 1
        left_node = dummy
        
        temp = rev(left_node.next, 0)

        left_node.next.next = right_node
        left_node.next = temp

        if left == 1:
            return temp
        
        else:
            return head



