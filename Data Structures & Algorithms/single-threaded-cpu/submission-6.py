class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_heap = [(task[0], task[1], e) for e, task in enumerate(tasks)]
        heapq.heapify(task_heap)
        q = deque()
        time = 0
        res = []

        def check_q(time):
            while q and q[-1][0] <= time:
                task = q.pop()
                heapq.heappush(task_heap, (time, task[1], task[2]))

        while task_heap or q:
            check_q(time)
            task = heapq.heappop(task_heap)
            res.append(task[2])
            if time < task[0]:
                time += (task[0] - time)
            time += task[1]

            while task_heap and task_heap[0][0] <= time:
                q.append(heapq.heappop(task_heap))
            
        return res