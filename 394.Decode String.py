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


# 2025/03/09
# Time complexity: O(N)
# Space complexity: O(N)
import string
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        idx = 0
        int_str = {str(i) for i in range(10)}
        letter_set = set(string.ascii_lowercase)
        while idx < len(s):
            cur = s[idx]
            idx += 1
            if cur != ']':
                stack.append(cur)
            else:
                str_part = ''
                digit_part = ''
                cond = False
                while stack:
                    x = stack.pop()
                    if not cond and x in letter_set:
                        str_part = x + str_part
                    elif not cond and x == '[':
                        cond = True
                        continue
                    elif x in int_str:
                        digit_part = x + digit_part
                    else:
                        pass

                    if (cond and x not in int_str) or (not stack):
                        if stack:
                            stack.append(x)
                        if not digit_part:
                            digit_part = '1'
                        stack.extend(list(int(digit_part) * str_part))
                        break
        return ''.join(stack)