class Solution:
    def intToRoman(self, num: int) -> str:
        data = [(1000,'M'), (900, 'CM'), (500,'D'), (400, 'CD'),
            (100,'C'), (90,'XC'), (50,'L'), (40,'XL'), (10,'X'),
            (9,'IX'), (5,'V'), (4,'IV'), (1,'I')]
        ans = ''
        for d in data:
            while num >= d[0]:
                ans += d[1]
                num -= d[0]
        return ans



        # data = [(1000,'M'), (500,'D'), (100,'C'), (50,'L'), (10,'X'), (5,'V'), (1,'I')]
        # ans = ''
        # for i, d in enumerate(data):
        #     while num // d[0]:
        #         if str(num)[0] =='4':
        #             num -= 4 * d[0]
        #             ans = ans + d[1] + data[i-1][1]
        #         elif str(num)[0] =='9':
        #             num -= 9 * data[i+1][0]
        #             ans = ans + data[i+1][1] + data[i-1][1]
        #         else:
        #             num = num - d[0]
        #             ans += d[1]
        # return ans
