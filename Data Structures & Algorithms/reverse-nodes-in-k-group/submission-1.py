# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def rev(head, count):
            if count == k-1:
                return head
            
            else:
                temp = rev(head.next, count+1)
                head.next.next = head 
                head.next = None

                return temp
                
        
        curr = head 
        grp = 0

        while curr and grp < k:
            curr = curr.next
            grp += 1
        
        if grp == k:
            prev_grp = self.reverseKGroup(curr, k)
            curr_grp = rev(head, 0)
            head.next = prev_grp
            head = curr_grp
        
        return head
