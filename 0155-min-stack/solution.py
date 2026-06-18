class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minVal) == 0:
            self.minVal.append(val)
        else:
            current_min = min(val, self.minVal[-1])
            self.minVal.append(current_min)


    def pop(self) -> None:
        self.stack.pop()
        self.minVal.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minVal[-1]
        
