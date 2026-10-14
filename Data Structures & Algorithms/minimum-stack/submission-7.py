class MinStack:
    stack = []
    minimum = None

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum != None and val < self.minimum:
            self.minimum = val
        elif self.minimum == None:
            self.minimum = val

    def pop(self) -> None:
        val = self.stack.pop()
        if self.minimum != None:
            if len(self.stack) > 0:
                self.minimum = min(self.stack)
            else:
                self.minimum = None
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum if self.minimum else 0
