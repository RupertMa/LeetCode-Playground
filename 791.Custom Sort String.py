class Solution:
    # Time complexity: O(N) N is the length of T
    # Space complexity: O(N)
    def customSortString(self, S: str, T: str) -> str:
        count = {s:0 for s in S}
        index = []
        for i,j in enumerate(T):
            if j in count:
                index.append(i)
                count[j] += 1
        p = 0
        l_T = list(T)
        for s in S:
            for i in range(count[s]):
                l_T[index[p]] = s
                p += 1
        return "".join(l_T)