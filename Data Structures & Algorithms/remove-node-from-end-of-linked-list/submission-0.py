# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        curr = ListNode()
        curr.next = head
        while i<n:
            curr = curr.next
            i += 1

        dummy = ListNode()
        dummy.next = head

        while curr.next:
            curr = curr.next
            dummy = dummy.next

        if dummy.next == head:
            dummy.next = dummy.next.next
            return dummy.next
        else:
            dummy.next = dummy.next.next
            return head
        

        
        
