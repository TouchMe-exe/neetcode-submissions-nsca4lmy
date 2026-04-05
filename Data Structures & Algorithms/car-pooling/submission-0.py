class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        startheap=[]
        endheap=[]
        for num,start,end in trips:
            heapq.heappush(startheap,(start,end,num))
        
        while startheap:
            cur=heapq.heappop(startheap)

            while endheap and endheap[0][0]<=cur[0]:
                capacity+=heapq.heappop(endheap)[1]
            
            if capacity < cur[2]:
                return False
            
            capacity-=cur[2]
            heapq.heappush(endheap,(cur[1],cur[2]))
        
        return True
