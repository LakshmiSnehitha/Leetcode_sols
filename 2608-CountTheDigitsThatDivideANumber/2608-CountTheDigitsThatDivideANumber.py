# Last updated: 8/1/2025, 9:07:12 AM
class Solution:
    def countDigits(self, n: int) -> int:
        l=[]
        s=n
        c=0
        while(n > 0):
            r=n%10
            l.append(r)
            n=n//10
        for i in  l:
            # return i
            if(s%i==0 and i!=0 ):
                c=c+1
        return c

