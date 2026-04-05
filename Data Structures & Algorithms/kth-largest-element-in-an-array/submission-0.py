class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        res=[]
        for i in range(len(nums)):
            res.append(heapq.heappop(nums))
        
        return res[-k]
