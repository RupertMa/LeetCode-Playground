class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people = [[h, k, k] for h,k in people]
        while len(people) > 0:
            min_k = len(people)
            min_h = float('inf')
            min_c = None
            for (h, k, c) in people:
                if k < min_k or (k== min_k and h < min_h):
                    min_k = k
                    min_h = h
                    min_c = c
            ans.append([min_h, min_c])
            people.remove([min_h, min_k, min_c])
            temp = []
            for (h, k, c) in people:
                if h <= min_h:
                    k -= 1
                temp.append([h, k, c])
            people = temp
        return ans

        # Time complexity: O(N**2)
        # Space complexity: O(N)
