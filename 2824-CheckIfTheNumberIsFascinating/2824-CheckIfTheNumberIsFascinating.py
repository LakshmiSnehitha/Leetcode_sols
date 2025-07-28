# Last updated: 7/28/2025, 3:28:47 PM
class Solution:
    def isFascinating(self, n: int) -> bool:
        s=str(n)+str(n*2)+str(n*3)
        if(len(s)!=9):
            return False
        return set(s)==set("123456789")
        # # p=1
        # # for i in n:
        # l.append(n)
        # l.append(n*2)
        # l.append(n*3)
        # c=(' '.join(str(item) for item in l)) 
        # # p=int(c)
        # # return c
        # if c in '123456789' or c not in '0':
        #     return True
        # else:
        #     return False

        