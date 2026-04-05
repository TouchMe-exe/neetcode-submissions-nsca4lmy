class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i in range(len(points)):
            val = math.sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1])
            heapq.heappush(min_heap, (val, points[i]))
        
        res = []
        for i in range(k):
            point = heapq.heappop(min_heap)
            res.append(point[1])
        
        return res