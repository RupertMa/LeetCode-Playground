class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 2:
            return True
        
        pointer = 1
        while pointer < len(A) and A[pointer-1] == A[pointer]:
            pointer += 1
        
        if pointer >= len(A):
            return True
        
        if A[pointer-1] < A[pointer]:
            while pointer < len(A):
                if A[pointer-1] > A[pointer]:
                    return False
                pointer += 1
            return True
        elif A[pointer-1] > A[pointer]:
            while pointer < len(A):
                if A[pointer-1] < A[pointer]:
                    return False
                pointer += 1
        
            return True
            