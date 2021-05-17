class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        right = []
        for i, j in enumerate(s):
            if j == '(':
                stack.append(i)
            elif j == ')':
                if stack:
                    prev = stack.pop()
                else:
                    right.append(i)
        remove = set(stack+right)
        return "".join([j for i,j in enumerate(s) if i not in remove])

        # Time complexity: O(N)
        # Sapce complexity: O(N)
