class StockSpanner:

    def __init__(self):
        self.stack = []
        self.res = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        i = len(self.stack)-1
        count = 0
        while i>-1 and price >= self.stack[i]:
            count += 1
            i -= 1
        self.res.append(count)
        return self.res[-1]




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)