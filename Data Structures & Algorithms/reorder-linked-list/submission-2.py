# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
        
        node = slow.next
        slow.next = None

        def reverse(head):

            if head == None or head.next == None:
                return head
            
            newhead = reverse(head.next)
            head.next.next = head
            head.next = None

            return newhead
        
        head2 = reverse(node)
        dummy = head

        i = 0

        while head2:
            if i%2 != 0:
                dummy = dummy.next
            else:
                temp = dummy.next
                dummy.next = head2
                head2 = head2.next
                dummy.next.next = temp
                dummy = dummy.next
            i += 1



        
