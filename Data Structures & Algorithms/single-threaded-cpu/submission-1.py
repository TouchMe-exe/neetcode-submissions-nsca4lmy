class PendingTask:
    def __init__(self, enqueue_time, processing_time, task_index):
        self.enqueue_time = enqueue_time
        self.processing_time = processing_time
        self.task_index = task_index
    
    def __lt__(self, other_task):
        return self.enqueue_time < other_task.enqueue_time

    def __repr__(self):
        return f"PendingTask({self.enqueue_time}, {self.processing_time}, {self.task_index})"

class WaitingTask:
    def __init__(self, enqueue_time, processing_time, task_index):
        self.enqueue_time = enqueue_time
        self.processing_time = processing_time
        self.task_index = task_index
    
    def __lt__(self, other_task):
        return (
            self.processing_time < other_task.processing_time
            or (
                self.processing_time == other_task.processing_time 
                and self.task_index < other_task.task_index
            )
        )

    def __repr__(self):
        return f"WaitingTask({self.enqueue_time}, {self.processing_time}, {self.task_index})"

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending_tasks = []
        waiting_tasks = []
        result = []
        for i, task in enumerate(tasks):
            pending_tasks.append(PendingTask(task[0], task[1], i))
        heapq.heapify(pending_tasks)
        current_time = 1
        while len(pending_tasks) or len(waiting_tasks):
            while (
                len(pending_tasks) != 0 
                and pending_tasks[0].enqueue_time <= current_time
            ):
                task = heapq.heappop(pending_tasks)
                heapq.heappush(waiting_tasks, WaitingTask(task.enqueue_time, task.processing_time, task.task_index))
            if len(waiting_tasks):
                task = heapq.heappop(waiting_tasks)
                result.append(task.task_index)
                current_time += task.processing_time
            else:
                current_time = pending_tasks[0].enqueue_time
        return result
        
        