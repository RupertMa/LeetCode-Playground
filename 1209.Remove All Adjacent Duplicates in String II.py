class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        dup = False
        stack = []
        counter = 0
        for i in s:
            #print(i, dup, stack)
            if stack and stack[-1] == i:
                counter += 1
            else:
                counter = 1
            stack.append(i)
            if counter >= k:
                dup = True
                while counter:
                    stack.pop()
                    counter -= 1
        if dup:
            return self.removeDuplicates("".join(stack), k)
        else:
            return "".join(stack)


        SC, st, i, j = list(s), [0], 1, 1
        while j < len(s):
            SC[i] = SC[j]
            if i == 0 or SC[i] != SC[i-1]: st.append(i)
            elif i - st[-1] + 1 == k: i = st.pop() - 1
            i += 1
            j += 1
        return "".join(SC[:i])


x = Solution()
print(x.removeDuplicates(s="deeedbbcccbdaa", k = 3))
print(x.removeDuplicates(s="abcd", k = 3))
print(x.removeDuplicates(s="pbbcggttciiippooaais", k = 2))
