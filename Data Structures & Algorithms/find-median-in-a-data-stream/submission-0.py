class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]


        

    def addNum(self, num: int) -> None:
        if not self.minheap and not self.maxheap:
            heapq.heappush(self.maxheap,-num)
        
        elif (len(self.minheap)+len(self.maxheap)==1):
            if (-self.maxheap[0]<=num):
                heapq.heappush(self.minheap,num)
            else:
                heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
                heapq.heappush(self.maxheap,-num)
        
        else:
            if (-self.maxheap[0]>num):
                heapq.heappush(self.maxheap,-num)
            else:
                heapq.heappush(self.minheap,num)
            
            if (len(self.maxheap)==len(self.minheap)+2):
                heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
            elif (len(self.minheap)==len(self.maxheap)+1):
                heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))

        

    def findMedian(self) -> float:
        n = len(self.maxheap)+len(self.minheap)
        if n==1 or n%2==1:
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0]+self.minheap[0])/2

                    
        