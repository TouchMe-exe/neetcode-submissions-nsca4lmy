class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        minheap=[]
        for i in range (1,len(points)):
            heapq.heappush(minheap,(abs(points[0][0]-points[i][0])+abs(points[0][1]-points[i][1]),i))
        
        visited=set()
        visited.add(0)

        total=0
        while len(visited)!=len(points):
            nxt_point=heapq.heappop(minheap)
            if nxt_point[1] in visited:
                continue
            total+=nxt_point[0]
            visited.add(nxt_point[1])

            for i in range(len(points)):
                if i in visited:
                    continue
                heapq.heappush(minheap,(abs(points[nxt_point[1]][0]-points[i][0])+abs(points[nxt_point[1]][1]-points[i][1]),i))
        
        return total