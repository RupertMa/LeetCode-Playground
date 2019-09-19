class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        median = (n-1) // 2
        left = self.sortArray(nums[:median+1])
        right = self.sortArray(nums[median+1:])
        sortedLst = self.mergeTwoSortedList(left, right)
        return sortedLst
            


    def mergeTwoSortedList(self, lst1, lst2):
        pointer1 = 0 ; pointer2 =0
        ans = []
        while pointer1 < len(lst1) and pointer2 < len(lst2):
            if  lst1[pointer1] <= lst2[pointer2]:
                ans.append(lst1[pointer1])
                pointer1 += 1
            else:
                ans.append(lst2[pointer2])
                pointer2 += 1
        if pointer1 < len(lst1) and pointer2 >= len(lst2):
            ans.extend(lst1[pointer1:])
        else:
            ans.extend(lst2[pointer2:])
        return ans