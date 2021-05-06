class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'{':'}', '(':')', '[':']'}
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                prev = stack.pop() if stack else "x"
                if i != opening.get(prev):
                    return False
        return not stack

        # Time complexity: O(N)
        # Space complexity: O(N)
