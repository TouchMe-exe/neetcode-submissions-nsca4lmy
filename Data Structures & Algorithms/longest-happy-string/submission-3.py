class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        def ishappy(s):
            return len(s)<3 or (s[-1] != s[-2] or s[-1] != s[-3])
        maxheap=[]
        if a:
            heapq.heappush(maxheap,(-a,"a"))
        if b:
            heapq.heappush(maxheap,(-b,"b"))
        if c:
            heapq.heappush(maxheap,(-c,"c"))

        res=""
        while maxheap:
            if len(maxheap)==1:
                e = heapq.heappop(maxheap)
                if ishappy(res+e[1]):
                    res = res + e[1]
                    if e[0] + 1:
                        heapq.heappush(maxheap, (e[0]+1, e[1]))
            else:
                e1 = heapq.heappop(maxheap)
                if ishappy(res + e1[1]):
                    res = res + e1[1]
                    if e1[0] + 1:
                        heapq.heappush(maxheap, (e1[0]+1, e1[1]))
                else:
                    e2 = heapq.heappop(maxheap)
                    res = res + e2[1]
                    if e2[0] + 1:
                        heapq.heappush(maxheap, (e2[0]+1, e2[1]))
                    heapq.heappush(maxheap, e1)
        return res
                
                    