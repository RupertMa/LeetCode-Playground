class Solution:
    def addToArrayForm(self, A, K):
        
        A = A[::-1]
        K = str(K)[::-1]
        n = len(A)
        m = len(K)
        pointer = 0
        temp = 0
        ans = []
        while pointer < max(m,n):
            if pointer < min(m,n):
                temp = temp + A[pointer] + int(K[pointer])
                ans.append(temp % 10)
                temp = temp // 10
            else:
                if m > n:
                    temp = temp + int(K[pointer])
                else:
                    temp = temp + A[pointer]
                ans.append(temp % 10)
                temp = temp // 10

            pointer += 1
        if temp:
            ans.append(temp)
        return ans[::-1]
