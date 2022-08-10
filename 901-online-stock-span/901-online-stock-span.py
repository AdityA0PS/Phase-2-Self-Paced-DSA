class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        days = 1
        while self.stk and self.stk[-1][0] <= price:
            days += self.stk.pop()[1]
        self.stk.append([price, days])
        return days