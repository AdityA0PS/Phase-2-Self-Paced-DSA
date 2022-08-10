class MinStack:

    def __init__(self):
        self.data = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.data.append(val)
        if self.minStack and self.minStack[-1] < val:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)
            
    def pop(self) -> None:
        self.data.pop(-1)
        self.minStack.pop(-1)
        
    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minStack[-1]