class MyStack:
    from collections import deque
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque([])
        self.queue2 = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        k = len(self.queue1) - 1
        while k:
            self.queue2.append(self.queue1.popleft())
            k -= 1
        ans = self.queue1.popleft()
        self.queue1 = self.queue2
        self.queue2 = deque([])
        return ans


    def top(self) -> int:
        """
        Get the top element.
        """
        k = len(self.queue1) - 1
        while k:
            self.queue2.append(self.queue1.popleft())
            k -= 1
        ans = self.queue1.popleft()
        self.queue2.append(ans)
        self.queue1 = self.queue2
        self.queue2 = deque([])
        return ans

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0
