class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        max_heap = [-f for f in count.values()]
        heapq.heapify(max_heap)

        q=deque()
        time=0
        while max_heap or q:
            if q and q[0][1]==time:
                temp=q.popleft()
                heapq.heappush(max_heap,temp[0])
            if max_heap:
                freq=heapq.heappop(max_heap)
                freq+=1
                qtime=time+n+1
                if freq!=0:
                    q.append((freq,qtime))
            time+=1

        return time






        




            
            


        