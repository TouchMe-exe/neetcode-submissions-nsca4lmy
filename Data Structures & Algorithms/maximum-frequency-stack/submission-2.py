class FreqStack:

    def __init__(self):
        self.max_heap = []
        self.freq_map = {}
        self.curr_time = 0

    def push(self, val: int) -> None:
        self.freq_map[val] = 1 + self.freq_map.get(val, 0)
        self.curr_time += 1
        heapq.heappush(self.max_heap, (-self.freq_map[val], -self.curr_time, val))
        
    def pop(self) -> int:
        freq , time, val = heapq.heappop(self.max_heap)
        self.freq_map[val] = self.freq_map.get(val) - 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()