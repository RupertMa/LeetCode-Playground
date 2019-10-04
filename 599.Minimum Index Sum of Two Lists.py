class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_d = {}
        lst_sum = 0x7FFFFFFF
        ans = []
        for idx, rest in enumerate(list1):
            list1_d[rest] = list1_d.get(rest,0) + idx
        for idx, rest in enumerate(list2):
            if rest in list1_d:
                if (list1_d[rest] + idx < lst_sum):
                    lst_sum = list1_d[rest] + idx
                    ans = [rest]
                elif list1_d[rest] + idx == lst_sum:
                    ans.append(rest)
        return ans