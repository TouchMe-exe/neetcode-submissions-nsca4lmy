class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        self.i += 1
        while self.stack and self.stack[-1][0]<=price:
            self.stack.pop()
        if self.stack:
            res = self.i - self.stack[-1][1]
        else:
            res = self.i
        self.stack.append((price, self.i))
        return res
        

            






# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)