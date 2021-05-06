class Solution:
    def decodeString(self, s: str) -> str:
        nums = [str(i) for i in range(10)]
        stack = []
        for i in s:
            if i == ']':
                temp = ''
                prev = stack.pop()
                while prev != '[':
                    temp = prev + temp
                    prev = stack.pop()
                k = ''
                num = stack.pop()
                while num in nums:
                    k = num + k
                    num = stack.pop() if stack else ''
                stack.extend([num]+int(k)*list(temp))
            else:
                stack.append(i)
        return ''.join(stack)

        # Time complexity: O(N)
        # Space complexity: O(N)
