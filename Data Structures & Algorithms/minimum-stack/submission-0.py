class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.minstack) == 0:
            self.stack.append(val)
            self.minstack.append(val)
            return
        elif val < self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        if len(self.minstack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minstack) > 0:
            return self.minstack[-1]
