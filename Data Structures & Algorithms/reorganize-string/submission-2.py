class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        max_heap=[(-cnt,elm) for elm,cnt in count.items()]
        heapq.heapify(max_heap)

        q=deque()
        time=0
        res=""

        while max_heap or q:
            
            if max_heap:
                freq,elm=heapq.heappop(max_heap)
                res=res+elm
                freq+=1
                qtime=time+1
                if freq:
                    q.append((freq,elm,qtime))
                    

            if q and q[0][2]==time:
                freq,elm,time=q.popleft()
                heapq.heappush(max_heap,(freq,elm))
            
            if not max_heap and q and q[0][2]!=time:
                return ""
            
            time+=1

        return res


