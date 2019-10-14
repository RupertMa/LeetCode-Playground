class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        lst_s = []
        lst_t = []
        for s in S:
            if s!='#':
                lst_s.append(s)
            else:
                lst_s and lst_s.pop()
        for t in T:
            if t!='#':
                lst_t.append(t)
            else:
                lst_t and lst_t.pop()
        return lst_s==lst_t
        