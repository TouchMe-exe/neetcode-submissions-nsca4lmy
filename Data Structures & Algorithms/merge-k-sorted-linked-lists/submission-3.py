# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeList(list1: Optional[ListNode],list2: Optional[ListNode]) -> Optional[ListNode]:
            
            if not list1:
                return list2
            if not list2:
                return list1

            if list1.val<=list2.val:
                list1.next=mergeList(list1.next,list2)
                return list1
            if list2.val<=list1.val:
                list2.next=mergeList(list1,list2.next)
                return list2
        if not lists:
            return None        
        res=lists[0]
        for i in range(1,len(lists)):
            res=mergeList(res,lists[i])
            
        
        return res


