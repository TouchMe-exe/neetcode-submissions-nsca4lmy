class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map={}
        for num in nums:
            Map[num]=1+Map.get(num,0)
        
        heap=[]

        for num in Map.keys():
            heapq.heappush(heap,(Map[num],num))
            if len(heap)>k:
              heapq.heappop(heap)  
        
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        

                   