class MinStack:

    def __init__(self):
        self.stack = []
        self.the_last_min = []        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.the_last_min :
            self.the_last_min.append(value)
        elif value <= self.the_last_min[-1] :
            self.the_last_min.append(value)

        return None

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.the_last_min[-1]:
            self.the_last_min.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.the_last_min :
            return 0
        return self.the_last_min[-1]
