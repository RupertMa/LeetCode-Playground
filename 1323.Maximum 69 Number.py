class Solution:
    def maximum69Number (self, num: int) -> int:
        str_nums = str(num)
        pos = str_nums.find('6')
        if pos != -1:
            return int(str_nums[:pos] + '9' + str_nums[pos+1:])
        return num