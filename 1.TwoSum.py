class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            newnums=nums[nums.index(i)+1:]
            for s in newnums:
                if i+s==target:
                    return [nums.index(i),newnums.index(s)+nums.index(i)+1]
#自己改出来了！没看参考答案！开心！

#算法效率又不够嘤嘤嘤        
#        c1=c2=0
#        for i in nums:
#            for s in nums[c1+1:]:
#                c2+=1
#                if i+s==target:
#                    return [c1,c2]
#            c2=c1+1
#            c1+=1

    # Approach 1: HashSet
    # Time complexity O(N)
    # Space complexity O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        S = {}
        for idx, num in enumerate(nums):
            S[num] = S.get(num,[]) + [idx]
            
        for num in nums:
            if (target - num) in S:
                if num == target - num and len(S[num])>=2:
                    return S[num][:2]
                elif num != target - num:
                    return [S[num][0],S[target - num][0]]
        return None

    # Approach 1: Sort + Two pointers
    # Time complexity O(NlogN)
    # Space complexity O(1) (theoretically, but not applicable for this problem)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted([(num, idx) for idx, num in enumerate(nums)])
        slow = 0 ; fast = 1
        while slow < len(nums) - 1:
            while fast < len(nums):
                if (nums[slow][0] + nums[fast][0]) == target:
                    return [nums[slow][1], nums[fast][1]]
                elif nums[slow][0] + nums[fast][0] < target:
                    fast += 1
                else:
                    break
            slow += 1
            fast = slow + 1
        return None
