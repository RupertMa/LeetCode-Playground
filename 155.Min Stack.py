class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and val == self.minStack[-1][0]:
            self.minStack[-1] = (val, self.minStack[-1][1]+1)
        elif (not self.minStack) or (val < self.minStack[-1][0]):
            self.minStack.append((val, 1))

    def pop(self) -> None:
        discard = self.stack.pop()
        if discard == self.minStack[-1][0]:
            count = self.minStack[-1][1] - 1
            if count:
                self.minStack[-1] = (discard, count)
            else:
                self.minStack.pop()
        return None


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1][0]
