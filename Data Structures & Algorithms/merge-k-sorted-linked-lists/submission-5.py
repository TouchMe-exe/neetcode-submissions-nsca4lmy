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

        def mergesort(l,li,ri) -> Optional[ListNode]:

            if li>ri:
                return None
            if li==ri:
                return l[ri]
            mid=li+(ri-li)//2
            left=mergesort(l,li,mid)
            right=mergesort(l,mid+1,ri)

            return mergeList(left,right)

        if not lists:
            return None
        return mergesort(lists,0,len(lists)-1)


        




